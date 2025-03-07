class Client:
    def __init__(self, id, name, cnp, birthdate):
        self.__id = id
        self.__name = name
        self.__cnp = cnp
        self.__birthdate = birthdate

    def get_id(self):
        return self.__id
    def get_cnp(self):
        return self.__cnp
    def get_birthdate(self):
        return self.__birthdate
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    def set_cnp(self, new_cnp):
        self.__cnp = new_cnp
    def set_birthdate(self, new_birthdate):
        self.__birthdate = new_birthdate

    def __str__(self):
        return f"Client ID: {self.__id}, Name: {self.__name}, CNP: {self.__cnp}, Birthdate: {self.__birthdate}"