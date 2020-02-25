class BitpwndException(Exception):
    pass


class ClientException(BitpwndException):
    pass


class BitwardenException(ClientException):
    pass
