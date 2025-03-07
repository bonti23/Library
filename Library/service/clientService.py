from domain.client import Client
from repository.clientRepository import RepositoryClient
from domain.validation import ClientValidation

class ClientService:
    def __init__(self, repository: RepositoryClient):
        self.__repository = repository

    def service_add_client(self, id, name, cnp, birthdate):
        validator = ClientValidation(self.__repository)
        client = Client(id, name, cnp, birthdate)
        validator.validate_client(client)
        return self.__repository.add_client(id, name, cnp, birthdate)

    def service_delete_client(self, index):
        self.__repository.delete_client(index)

    def service_modify_client(self, number, name, cnp, birthdate):
        self.__repository.modify_client(number, name, cnp, birthdate)

    def service_find_client(self, id):
        return self.__repository.find_client(id)

    def service_undo(self):
        self.__repository.undo()

    def service_print_clients(self):
        return self.__repository.print_clients()