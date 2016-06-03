import sql_manager
from helpers import StrongPasswordException, InvalidInput, UnsuccessfulLoginException
import messages


def main_menu():
    message_welcome()
    while True:
        user_input = input("$$$>")
        try:
            commands[user_input]()
        except InvalidInput as e:
            print(e)


def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    try:
        sql_manager.register(username, password)
        return "Registration siccessfull"
    except StrongPasswordException as e:
        print(e)


def helpp():
    return messages.HELP


def exit():
    return exit()


def message_welcome():
    return messages.WELCOME


def login():
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        try:
            sql_manager.login(username, password)
            logged_menu(username)
        except UnsuccessfulLoginException as e:
            print(e)


# def message_logged_user(logged_user):
#     return "Welcome you are logged in as: {}".\
#             format(logged_user.get_username())


# def info(logged_user):
#     return "You are: {} \nYour id is: {}/n Your balance is: {}".\
#             format(logged_user.get_username(), str(logged_user.get_id()), str(logged_user.get_balance()) + '$')


# def changepass(logged_user):
#     new_pass = input("Enter your new password: ")
#     new_pass = sql_manager.hash_my_password(new_pass, None)
#     return sql_manager.change_pass(new_pass, logged_user)


# def change_message(logged_user):
#     new_message = input("Enter your new message: ")
#     return sql_manager.change_message(new_message, logged_user)


# def show_message(logged_user):
#     return logged_user.get_message()


def logged_menu_help():
    return "info - for showing account info\n\
            changepass - for changing passowrd\n\
            change-message - for changing users message\n\
            show-message - for showing users message"


def logged_menu(logged_user):
    message_logged_user(logged_user)
    while True:
        logged_user_input = input("Logged>>")
        if logged_user_input == "help":
            logged_menu_help()
        else:
            return commands[logged_user_input](logged_user)


commands = {
    "register": register,
    # "info": info,
    "login": login,
    # "changepass": changepass,
    # "change-message": change_message,
    # "show-message": show_message,
    # "help": helpp,
    # "exit": exit
        }


def main():
    sql_manager.create_database()
    main_menu()

if __name__ == '__main__':
    main()
