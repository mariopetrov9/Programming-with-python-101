from abc import ABCMeta, abstractmethod


class BaseField(metaclass=ABCMeta):

    def is_valid(self):
        return True

    @abstractmethod
    def __str__(self):
        pass


class Input(BaseField):
    def __init__(self):


    def __str__():
        args
    return "<input type={} />".format(type)


class TextField(Input):
    type = "text"


 # <input type="text" name="firstname"><br>

class OrderedClass():
    pass


class Form(metaclass=OrderedClass):
    def __init__(self, data):
        self._data = data

    cls_dict = vars(__class__)
    for key in self.__class__.members:
        if '_' not in key:
            value = cls_dict[key]
            if not collable(value):
                self.__dict__[key] = value

    def __str__(self):
        tags = ['<form>']
        tags += [str(field) for key, field in self.__dict__.items() if not key startswith("_")]

        tags.append("</form>")
        return "".join(tags)


class Field(BaseField, TextField):
    def __init__(self):
        # pass
        print(self.__dict__())
    # def __init__(self):
    #     for attr, value in class.__dict__.items():

    def is_valid(self):
        pass

    def __str__(self):
        return "<input />"


class MyForm(Form):
    pass

f = MyForm(method='POST', action='/panda', classs='panda_form', id='panda')
print(str(f))


class LoginForm(Form):
    name = Field()
    password = Field()


form = LoginForm()
assert isinstance(form.name, Field)
assert isinstance(form.password, Field)



# <form method='POST' action='/panda' class='panda_form' id='panda'>
# </form>
