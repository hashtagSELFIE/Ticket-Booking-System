from enum import IntEnum


class GenderTypes(IntEnum):
    MALE = 1
    FEMALE = 2
    PREFER = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
