import sqlite3
from client import Client
import helpers
import messages
from settings import SQL_STRUCTURE_FILE
import datetime


db = sqlite3.connect("bank.db")
db.row_factory = sqlite3.Row
cursor = db.cursor()


def create_database():
    with open(SQL_STRUCTURE_FILE, 'r') as f:
        query = f.read()

    cursor.executescript(query)


def register(username, password):
    validator = helpers.validate(username, password)

    if not validator.is_valid(password):
        raise helpers.StrongPasswordException(messages.STRONG_PASSWORD)

    hashed_password, salt = helpers.hash_my_password(password)
    cursor.execute('''INSERT INTO clients (username, password, salt)
                      VALUES (?, ?, ?)''', (username, hashed_password, salt))
    db.commit()


def get_id_from_username(username):
    cursor.execute('''SELECT id
                      FROM clients
                      WHERE username = ?''', (username, ))
    for row in cursor.fetchone():
        return row['id']


def create_login_attempt(username, status=None):
    client_id = get_id_from_username(username)
    time = datetime.datetime.now()
    cursor.execute('''INSERT INTO login_attempts (client_id, status, time)
                      VALUES(?, ?, ?)''', (client_id, "SUCCESS", time))


def login(username, password):
    if _login(username, password):
        create_login_attempt(username, status="SUCCESS")
    else:
        create_login_attempt(username, status="FAILURE")


def _login(username, password):
    cursor.execute("""SELECT salt
                    FROM clients
                    WHERE username = ?""", (username,))
    salt = cursor.fetchone()

    if salt is None:
        raise helpers.UnsuccessfulLoginException(messages.UNCUCCESSFUL_LOGIN)

    hashed_pass, _ = helpers.hash_my_password(password, salt=salt['salt'])
    cursor.execute('''SELECT id, username, balance, message
                        FROM clients
                        WHERE username = ? AND password = ?
                        LIMIT 1''', (username, hashed_pass))
    row = cursor.fetchone()
    print(row["id"])
    if(row):
        return Client(row["id"], row["username"], row["balance"], row["message"])
    else:
        raise helpers.UnsuccessfulLoginException(messages.UNCUCCESSFUL_LOGIN)


def change_pass(new_pass, logged_user):
    cursor.execute('''UPDATE clients
                      SET password = ?
                      WHERE id = ?''', (new_pass, logged_user.get_id()))
    db.commit()


def change_message(new_message, logged_user):
    cursor.execute('''UPDATE clients
                      SET message = ?
                      WHERE id = ?''', (new_message, logged_user.get_id()))
    db.commit()
    return logged_user.set_message(new_message)


