import messages


class InvalidInput(Exception):
    messages.INVALID_INPUT
    pass


class StrongPasswordException(Exception):
    messages.STRONG_PASSWORD
    pass


class UnsuccessfulLogin(Exception):
    messages.UNCUCCESSFUL_LOGIN
    pass


class ClientAlreadyRegistered(Exception):
    pass


class UserBlocked(Exception):
    pass


class ClientNotRegistered(Exception):
    pass
