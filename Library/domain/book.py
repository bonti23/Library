class Book:
    def __init__(self, id, title, author, pages):
        self.__id = id
        self.__title = title
        self.__author = author
        self.__pages = pages

    def get_id(self):
        return self.__id
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_pages(self):
        return self.__pages
    def set_title(self, new_title):
        self.__title = new_title
    def set_author(self, new_author):
        self.__author = new_author
    def set_pages(self, new_pages):
        self.__pages = new_pages

    def __str__(self):
        return f"Book ID: {self.__id}, Title: {self.__title}, Author: {self.__author}, Pages: {self.__pages}"
