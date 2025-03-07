from service.bookService import BookService
from service.clientService import ClientService
from service.rentalService import RentalService
from repository.bookRepository import bookRepository
from repository.clientRepository import RepositoryClient
from repository.rentalRepository import RentalRepository
from ui.Console import LibraryUI

repo1 = bookRepository("data/books.txt")
service1 = BookService(repo1)

repo2=RepositoryClient("data/clients.txt")
service2 = ClientService(repo2)

repo3=RentalRepository("data/rentals.txt")
service3 = RentalService(repo3)

controller = LibraryUI(service1, service2, service3)
controller.runner()
