import string


class HasAtleastOneSymbolValidation:
    def __init__(self):
        self.__symbols = list(string.punctuation)

    def __call__(self, string):
        return any([ch in self.__symbols for ch in string])


class LengthValidation:
    def __init__(self, length):
        self.__length = length

    def __call__(self, string):
        return len(string) >= self.__length


class PasswordValidator:
    def __init__(self):
        self.__validators = []

    def is_valid(self, password):
        return all([v(password) for v in self.__validators])

    def add_validation(self, validator):
        self.__validators.append(validator)
        return self


def validate(password, username):
    validator = password_validator.PasswordValidator()
    validator\
        .add_validation(password_validator.LengthValidation(8))\
        .add_validation(password_validator.HasAtleastOneSymbolValidation())\
        .add_validation(lambda string: any([s.upper() for s in password]))\
        .add_validation(lambda string: any([x.isdigit() for x in password]))\
        .add_validation(lambda string: password in username)
    # validator.add_validation(lambda string: string.count("&") == 2
    return validator.is_valid(password)


def generate_salt():
    rbits = random.getrandbits(256)
    m = hashlib.sha256()
    m.update(str(rbits).encode('utf-8'))
    return m.hexdigest()


def hash_my_password(password, salt=None):
    m = hashlib.sha256()
    if salt is None:
        salt = generate_salt()
    m.update((password + salt).encode('utf-8'))
    return (m.hexdigest(), salt)


def get_hashed_password(password):
    cursor.execute('''SELECT password
                      FROM clients
                      WHERE username = ?''', (password,))
    db.commit()
    row = cursor.fetchone()

    if(row):
        return row['password']


def login_password(password):
    hashed_password = hash_my_password(password, None)
    return hashed_password == get_hashed_password(password)

