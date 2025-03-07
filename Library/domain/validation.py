from datetime import datetime

from domain import book
from repository.bookRepository import bookRepository
from repository.clientRepository import RepositoryClient


class BookValidation:
    def __init__(self, book_repository:bookRepository):
        self.book_repository=book_repository
    def validate_book(self, book):
        errors = []
        if self.book_repository.find_book(book.get_id()):
            errors.append('f"Book with ID {book.get_id()} already exists!"')
        if len(book.get_author())<=0:
            errors.append("Invalid author!")
        if len(book.get_title())<=0:
            errors.append("Invalid title!")
        if int(book.get_pages())<=10:
            errors.append("Not enough pages!")
        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)

class ClientValidation:

    def __init__(self, client_repository:RepositoryClient):
        self.client_repository = client_repository

    def validate_client(self, client):
        errors = []
        if self.client_repository.find_client(client.get_id()):
            errors.append(f"Client with ID {client.get_id()} already exists!")
        if len(client.get_cnp())!=13:
            errors.append("Invalid cnp!")
        if len(client.get_name())<=0:
            errors.append("Invalid name!")
        birthdate = client.get_birthdate()
        if birthdate == "":
            errors.append("Birthdate cannot be empty!")
        else:
            try:
                datetime.strptime(birthdate, "%d/%m/%Y")
            except ValueError:
                errors.append("Invalid birthdate format! Please use DD/MM/YYYY.")
        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)