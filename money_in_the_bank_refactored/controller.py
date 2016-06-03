from models import *
import exceptions
import helpers
import messages
import datetime
from user import User
import settings
from sqlalchemy import update


# class MainController:

#     def __init__(self, session):
#         self.session = session

#     def __commit(self):
#         self.session.commit()

#     def __commit_object(self, obj):
#         self.session.add(obj)
#         self.__commit()

#     def __commit_objects(self, objects):
#         self.session.add_all(objects)
#         self.__commit()


class RegisterController:
    def __init__(self, session):
        self.__session = session
        self.__username = None
        self.__password = None
        self.__balance = None

    def validate(self):
        validator = helpers.validate(self.__username, self.__password)

        if not validator.is_valid(self.__password):
            raise exceptions.StrongPasswordException(messages.STRONG_PASSWORD)
        return True

    def check_if_user_not_in_BD(self, username):
        user = self.__session.query(Client).\
            filter(Client.username == username).first()

        if user is not None:
            raise exceptions.ClientAlreadyRegistered('Client already registered')
            return False
        return True

    def register(self, username, password, balance):
        if self.check_if_user_not_in_BD(username):
            self.__username = username
            self.__password = password
            self.__balance = balance
            if self.validate():
                hashed_password, salt = helpers.hash_my_password(password)
                client = Client(username=username, password=hashed_password, balance=self.__balance, salt=salt)
                self.__session.add(client)
                self.__session.commit()


class LoginController:
    def __init__(self, session):
        self.__session = session
        self.__username = None
        self.__password = None
        self.__client_id = None
        self.__balance = None

    def login(self, username, password):
        self.__username = username
        self.__password = password
        self.__client_id = int(self.get_user_id())
        self.__balance = int(self.get_balance_for_user())

        if not self.check_client_in_DB():
            raise exceptions.ClientNotRegistered(messages.CLIENT_NOT_REGISTERED)

        if self.is_blocked():
            raise exceptions.UserBlocked(messages.BLOCKED_USER)

        if self._login():
            self.user = User(self.__client_id, self.__username, self.__balance)
            self.create_login_attempt(status="SUCCESS")
        else:
            self.create_login_attempt(status="FAILURE")
            self.block_if_necessary()
            raise exceptions.\
                UnsuccessfulLogin(messages.UNCUCCESSFUL_LOGIN)
        return self.user

    def get_balance_for_user(self):
        return self.__session.query(Client.balance).\
                    filter(Client.id == self.__client_id).first()[0]

    def get_user_id(self):
        return self.__session.query(Client.id).\
                   filter(Client.username == self.__username).first()[0]

    def create_login_attempt(self, status=None):
        time = datetime.datetime.now()

        login_attempt = Login_attempts(client_id=self.__client_id, attempt_status=status, time=time)
        self.__session.add(login_attempt)
        self.__session.commit()

    def get_salt_from_DB(self):
        salt = self.__session.query(Client.salt).\
               filter(Client.username == self.__username).first()
        if salt is None:
            raise exceptions.\
                  UnsuccessfulLoginException(messages.UNCUCCESSFUL_LOGIN)
        return salt

    def check_hashed_passwords(self, salt):
        hashed_pass, _ = helpers.hash_my_password(self.__password, salt=salt[0])
        pass_from_base, _ = self.\
            __session.query(Client.password, Client.salt).\
            filter(Client.username == self.__username).first()
        return hashed_pass == pass_from_base

    def check_client_in_DB(self):
        if self.__client_id is not None:
            return True
        return False

    def _login(self):
        salt = self.get_salt_from_DB()
        return self.check_hashed_passwords(salt)

    def check_number_of_failures(self):
        list_attempts = self.__session.\
            query(Login_attempts.attempt_status).\
            filter(Login_attempts.client_id == self.__client_id).\
            order_by(Login_attempts.id.desc()).\
            limit(settings.BLOCK_AFTER_N_ATTEMPTS).all()
        if len(list_attempts) < settings.BLOCK_AFTER_N_ATTEMPTS:
            return
        should_block = all([elem[0] == 'FAILURE' for elem in list_attempts])
        if should_block:
            return True
        return False

    def block_if_necessary(self):
        if not self.check_number_of_failures():
            return
        self.block_user()

    def block_user(self):
        self.create_login_attempt(status="BLOCKED")
        block_start = datetime.datetime.now()
        block_end = block_start + datetime.\
            timedelta(seconds=settings.BLOCKING_TIME)
        blocked_user = Blocked_users(client_id=self.__client_id, block_start=block_start, block_end=block_end)
        self.__session.add(blocked_user)
        self.__session.commit()

    def is_blocked(self):
        block_end = self.__session.\
            query(Blocked_users.block_end).\
            filter(Blocked_users.client_id == self.__client_id).\
            order_by(Blocked_users.block_end.desc()).first()
        if block_end is None:
            return False

        return block_end[0] > datetime.datetime.now()

    def changepass(self, new_pass):
        hashed_pass, salt = helpers.hash_my_password(new_pass)
        self.__session.query(Client).filter(Client.id == self.__client_id).\
            update({'password': hashed_pass, 'salt': salt})
        self.__session.commit()


