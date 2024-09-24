class RedirectionError(Exception):
    pass


class CommandNotFoundError(Exception):
    pass


class FlagError(Exception):
    pass


class FlagValueError(Exception):
    pass


class FileAlreadyExistsError(Exception):
    pass
