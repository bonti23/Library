from domain.book import Book
from repository.bookRepository import bookRepository
from domain.validation import BookValidation
class BookService:
    def __init__(self, repository: bookRepository):
        self.__repository = repository
    def service_add_book(self, id, title, author, pages):
        validator=BookValidation(self.__repository)
        book=Book(id, title, author, pages)
        validator.validate_book(book)
        self.__repository.add_book_repository(id, title, author, pages)
        
    def service_delete_book(self, id):
        self.__repository.delete_book(id)

    def service_modify_book(self, id, title, author, pages):
        self.__repository.modify_book(id, title, author, pages)

    def service_find_book(self, id):
        return self.__repository.find_book(id)

    def service_undo(self):
        self.__repository.undo()

    def service_print_books(self):
        return self.__repository.printBooks()

    def service_find_books_by_author(self, author):
        same_author=[]
        books=self.__repository.read_book_from_file()
        for book in books:
            if book.author == author:
                same_author.append(book)
        return same_author
