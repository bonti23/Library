from domain.client import Client
from domain.book import Book
from repository.rentalRepository import RentalRepository

class RentalService:
    def __init__(self, repository: RentalRepository):
        self.__repository = repository

    def service_rent_book(self, book_id: str, client_id: str):
        self.__repository.rent(Book(book_id, "", "", ""), Client(client_id, "", "", ""))
    def service_return_book(self, book_id: str, client_id: str):
        self.__repository.return_book(Book(book_id, "", "", ""), Client(client_id, "", "", ""))

    def service_find_rentals_by_client(self, client_id: str):
        return self.__repository.find_rentals_by_client(Client(client_id, "", "", ""))

    def service_find_rentals_by_book(self, book_id: str):
        return self.__repository.find_rentals_by_book(Book(book_id, "", "", ""))

    def service_undo(self):
        self.__repository.undo()

    def service_print_rentals(self):
        return self.__repository.print_rentals()
