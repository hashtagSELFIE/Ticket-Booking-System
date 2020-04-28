from django.contrib.auth.models import User
from enum import IntEnum


class GenderTypes(IntEnum):
    MALE = 1
    FEMALE = 2
    PREFER = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


def prepare_context(request, show_navbar=True):
    context = {
        'show_navbar': show_navbar
    }

    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        context['current_user'] = user

    return context
