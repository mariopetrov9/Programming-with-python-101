from .models import User
from django.core.exceptions import ObjectDoesNotExist


def user_exists(email):
    try:
        User.objects.get(email=email)
        return True
    except ObjectDoesNotExist:
        return False


# def user_in_session(email):
#     try:
#         request.session[email] = email
#         return True
#     except ObjectDoesNotExist:
#         return False

def is_logged(email, password):
    try:
        User.objects.get(email=email, password=password)
        return True
    except ObjectDoesNotExist:
        return False
