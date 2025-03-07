from service.bookService import BookService
from service.clientService import ClientService
from service.rentalService import RentalService

class LibraryUI:
    def __init__(self, book_service: BookService, client_service: ClientService, rental_service: RentalService):
        self.__book_service = book_service
        self.__client_service = client_service
        self.__rental_service = rental_service
        self.__undo_stack = []

    def menu(self):
        print("MENU LIBRARY")
        print("1. add a book.")
        print("2. delete o book.")
        print("3. modify a book.")
        print("4. find a book.")
        print("5. add a client.")
        print("6. delete a client.")
        print("7. modify a client.")
        print("8. find a client.")
        print("9. rent a book.")
        print("10. return a book.")
        print("11. books rented by a client.")
        print("12. clients who rented a certain book.")
        print("13. undo.")
        print("14. books that have the same author.")
        print("15. close the application.")

    def add_book(self):
        id = input("id: ")
        title = input("title: ")
        author = input("author: ")
        pages = input("number of pages: ")
        try:
            self.__book_service.service_add_book(id, title, author, pages)
            self.__undo_stack.append(self.__book_service.service_undo)
        except ValueError as e:
            print(e)

    def delete_book(self):
        id = input("id: ")
        try:
            self.__book_service.service_delete_book(id)
            self.__undo_stack.append(self.__book_service.service_undo)
        except ValueError as e:
            print(e)

    def modify_book(self):
        id = input("id: ")
        title = input("title: ")
        author = input("author: ")
        pages = input("number of pages: ")
        self.__book_service.service_modify_book(id, title, author, pages)
        self.__undo_stack.append(self.__book_service.service_undo)

    def add_client(self):
        id = input("id: ")
        name = input("name: ")
        cnp = input("cnp: ")
        birthdate = input("birthdate: ")
        try:
            self.__client_service.service_add_client(id, name, cnp, birthdate)
            self.__undo_stack.append(self.__client_service.service_undo)
        except ValueError as e:
            print(e)

    def delete_client(self):
        index = int(input("index: "))
        self.__client_service.service_delete_client(index)
        self.__undo_stack.append(self.__client_service.service_undo)

    def modify_client(self):
        index = int(input("index: "))
        name = input("name: ")
        cnp = input("cnp: ")
        birthdate = input("birthdate: ")
        self.__client_service.service_modify_client(index, name, cnp, birthdate)
        self.__undo_stack.append(self.__client_service.service_undo)

    def rent_book(self):
        book_id = input("Id carte: ")
        client_id = input("Id client: ")
        try:
            self.__rental_service.service_rent_book(book_id, client_id)
            self.__undo_stack.append(self.__rental_service.service_undo)
        except ValueError as e:
            print(e)

    def return_book(self):
        book_id = input("id book: ")
        client_id = input("id client: ")
        try:
            self.__rental_service.service_return_book(book_id, client_id)
            self.__undo_stack.append(self.__rental_service.service_undo)
        except ValueError as e:
            print(e)

    def undo(self):
        if self.__undo_stack:
            last_action = self.__undo_stack.pop()
            last_action()
        else:
            print("There is no action to undo!")

    def find_client(self):
        client_id = input("id: ")
        client=self.__client_service.service_find_client(client_id)
        print(client)

    def find_book(self):
        book_id = input("id: ")
        book=self.__book_service.service_find_book(book_id)
        print(book)

    def find_rentals_by_client(self):
        client_id = input("id client: ")
        rentals=self.__rental_service.service_find_rentals_by_client(client_id)
        if rentals:
            print(f"Rentals for id_client {client_id}:")
            for rental in rentals:
                book = self.__book_service.service_find_book(rental[0])
                print(f"Book: {book} (id: {rental[0]})")
        else:
            print(f"No rentals for the client with id: {client_id}.")

    def find_rentals_by_book(self):
        book_id = input("id book: ")
        rentals=self.__rental_service.service_find_rentals_by_book(book_id)
        if rentals:
            print(f"Rentals for book_id {book_id}:")
            for rental in rentals:
                client = self.__client_service.service_find_client(rental[1])
                print(f"Client: {client} (id: {rental[1]})")
        else:
            print(f"No rentals for the book with id {book_id}.")

    def find_same_author(self):
        author = input("Author: ")
        books=self.__book_service.service_find_books_by_author(author)
        for book in books:
            print(book)

    def runner(self):
        self.menu()
        while True:
            choice = input("Choose an option: ")
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.delete_book()
            elif choice == "3":
                self.modify_book()
            elif choice == "4":
                self.find_book()
            elif choice == "5":
                self.add_client()
            elif choice == "6":
                self.delete_client()
            elif choice == "7":
                self.modify_client()
            elif choice == "8":
                self.find_client()
            elif choice == "9":
                self.rent_book()
            elif choice == "10":
                self.return_book()
            elif choice == "11":
                self.find_rentals_by_client()
            elif choice == "12":
                self.find_rentals_by_book()
            elif choice == "13":
                self.undo()
            elif choice == "14":
                self.find_same_author()
            elif choice == "15":
                print("Closed application!")
                break
            else:
                print("Invalid option!")
