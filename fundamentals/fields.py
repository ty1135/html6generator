from .utils import Singleton


class RequiredField(metaclass=Singleton):
    pass


class RequiredFieldError(Exception):
    pass


def validate_field(a_dict):
    for k in a_dict:
        if a_dict[k] is RequiredField():
            raise RequiredFieldError('{} is required'.format(k))
        elif isinstance(a_dict[k], dict):
            validate_field(a_dict[k])
