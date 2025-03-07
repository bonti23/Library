from domain.book import Book

class bookRepository:
    def __init__(self, filename):
        self.__filename = filename
        self.__previous = [] #for undo

    def read_book_from_file(self):
        f = open(file=self.__filename, mode="r")
        books = []
        lines = f.readlines()
        for line in lines:
            params = line.split(",")
            params = [param.strip() for param in params]
            id = params[0]
            title = params[1]
            author = params[2]
            pages = params[3]
            book = Book(id, title, author, pages)
            books.append(book)
        f.close()
        return books

    def write_book_to_file(self, books):
        with open(file = self.__filename, mode = "w") as f:
            for book in books:
                params = (book.get_id(), book.get_title(), book.get_author(), book.get_pages())
                params = [str(param) for param in params]
                line = ", ".join(params) + "\n"
                f.write(line)

    def add_book_repository(self, id, title, author, pages):
        books=self.read_book_from_file()
        copy=books[:]
        books.append(Book(id, title, author, pages))
        self.write_book_to_file(books)
        self.__previous.append(copy)

    def delete_book(self, index):
        books=self.read_book_from_file()
        copy=books[:]
        i=int(index)
        if 0 <= i <= len(books):
            del books[i-1]
            self.write_book_to_file(books)
            self.__previous.append(copy)
        else:
            raise ValueError("Index out of range")


    def modify_book(self, number, title, author, pages):
        books=self.read_book_from_file()
        copy=books[:]
        n=int(number)
        if n <= len(books) and n >= 0:
            books[n-1].set_title(title)
            books[n-1].set_author(author)
            books[n-1].set_pages(pages)
            self.write_book_to_file(books)
            self.__previous.append(copy)
            return books[n-1]
        return None

    def find_book(self, id):
        books=self.read_book_from_file()
        for book in books:
            if int(book.get_id()) == int(id):
                return book
        return None

    def undo(self):
        if self.__previous:
            before = self.__previous.pop()
            self.write_book_to_file(before)
        else:
            return None

    def printBooks(self):
        books=self.read_book_from_file()
        return books
