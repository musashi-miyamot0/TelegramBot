'''main module for fixed error or for summon errors'''


class BaseClassExpetions(Exception):
    '''Raised when an attribute is not found in a class.'''


class FailedToEnterContext(BaseClassExpetions):
    pass
