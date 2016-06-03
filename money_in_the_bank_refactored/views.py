from exceptions import *
import messages
import getpass


def helpp():
    return messages.HELP


def exit():
    return exit()


def message_welcome():
    return messages.WELCOME


class MainView:
    def __init__(self, reg_controller, log_controller):
        # self.main_controller = main_controller
        self.reg_controller = reg_controller
        self.log_controller = log_controller
        self.logged_user = None
        self.__active = True
        self.commands = {
            "register": self.register,
            "info": self.info,
            "login": self.login,
            "changepass": self.changepass,
            # "change-message": change_message,
            "show-message": self.show_message,
            "help": self.not_logged_help,
            "exit": self.exit
                }

    def main_menu(self):
        message_welcome()
        while self.__active is True:
            user_input = input("$$$>")
            try:
                self.commands[user_input]()
            except InvalidInput as e:
                print(e)

    def register(self):
        username = input("Enter your username: ")
        password = getpass.getpass(prompt='Enter your password: ')
        balance = input("Enter your balance: ")
        try:
            self.reg_controller.register(username, password, balance)
            return "Registration siccessfull"
        except StrongPasswordException as e:
            print(e)

    def login(self):
            username = input("Enter your username: ")
            password = getpass.getpass(prompt='Enter your password: ')
            try:
                self.logged_user =\
                    self.log_controller.login(username, password)
                self.logged_menu()
            except UnsuccessfulLogin as e:
                print(e)
            except UserBlocked as e:
                print(e)
            except ClientNotRegistered as e:
                print(e)

    def message_logged_user(self):
        return messages.LOGIN_AS.\
                format(self.logged_user.get_username())

    def logged_menu(self):
        print(self.message_logged_user())
        while True:
            logged_user_input = input("Logged>>")
            if logged_user_input == "help":
                print(messages.LOGGED_MENU)
            elif logged_user_input == "exit":
                break
            else:
                self.commands[logged_user_input]()

    def show_message(self):
        return self.logged_user.get_message()

    def not_logged_help(self):
        print(messages.NOT_LOGGED_HELP)
        return messages.NOT_LOGGED_HELP

    def exit(self):
        return self.__active is False

    def info(self):
        message = "You are: {} \nYour id is: {}\nYour balance is: {}$".\
                format(self.logged_user.get_username(), str(self.logged_user.get_id()), self.logged_user.get_balance())
        print(message)
        return message

    def changepass(self):
        new_pass = input("Enter your new password: ")
        return self.log_controller.changepass(new_pass)


# def change_message(logged_user):
#     new_message = input("Enter your new message: ")
#     return sql_manager.change_message(new_message, logged_user)
