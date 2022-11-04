from enum import Enum


class choice_operation_type(Enum):
    ADDITION = '1'
    SUBTRACTION = '2'
    MULTIPLICATION = '3'
    DIVISION = '4'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
