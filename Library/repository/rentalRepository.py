from domain.client import Client
from domain.book import Book

class RentalRepository:
    def __init__(self, filename):
        self.__filename = filename
        self.__previous = []  # For undo

    def read_rentals_from_file(self):
        with open(self.__filename, "r") as file:
            rentals = []
            lines = file.readlines()
            for line in lines:
                params = line.strip().split(",")
                book_id, client_id = params[0], params[1]
                rentals.append((book_id, client_id))
        return rentals

    def write_rentals_to_file(self, rentals):
        rentals = list(set(rentals))
        with open(self.__filename, "w") as file:
            for rental in rentals:
                line = f"{rental[0]},{rental[1]}\n"
                file.write(line)

    def rent(self, book: Book, client: Client):
        rentals = self.read_rentals_from_file()
        copy = rentals[:]
        if (book.get_id(), client.get_id()) not in rentals:
            rentals.append((book.get_id(), client.get_id()))
            self.write_rentals_to_file(rentals)
            self.__previous.append(copy)
            return rentals[-1]
        else:
            raise ValueError("Book already rented by this client!")

    def return_book(self, book: Book, client: Client):
        rentals = self.read_rentals_from_file()
        copy = rentals[:]
        if (book.get_id(), client.get_id()) in rentals:
            rentals.remove((book.get_id(), client.get_id()))
            self.write_rentals_to_file(rentals)
            self.__previous.append(copy)
        else:
            raise ValueError("Book not rented by this client!")

    def find_rentals_by_client(self, client: Client):
        rentals = self.read_rentals_from_file()
        return [rental for rental in rentals if rental[1] == client.get_id()]


    def find_rentals_by_book(self, book: Book):
        rentals = self.read_rentals_from_file()
        return [rental for rental in rentals if rental[0] == book.get_id()]

    def undo(self):
        if self.__previous:
            before = self.__previous.pop()
            self.write_rentals_to_file(before)
        else:
            return None

    def print_rentals(self):
        return self.read_rentals_from_file()

