from rolepermissions.roles import AbstractUserRole


class Autor(AbstractUserRole):
    available_permissions = {}


class Leitor(AbstractUserRole):
    available_permissions = {}