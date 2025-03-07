from domain.client import Client

class RepositoryClient:
    def __init__(self, filename):
        self.__filename = filename
        self.__previous = []  # For undo

    def read_clients_from_file(self):
        with open(self.__filename, "r") as file:
            clients = []
            lines = file.readlines()
            for line in lines:
                params = line.strip().split(",")
                id, name, cnp, birthdate = params[0], params[1], params[2], params[3]
                client = Client(id, name, cnp, birthdate)
                clients.append(client)
        return clients

    def write_clients_to_file(self, clients):
        with open(self.__filename, "w") as file:
            for client in clients:
                params = [client.get_id(), client.get_name(), client.get_cnp(), client.get_birthdate()]
                line = ", ".join(params) + "\n"
                file.write(line)

    def add_client(self, id, name, cnp, birthdate):
        clients = self.read_clients_from_file()
        copy = clients[:]
        clients.append(Client(id, name, cnp, birthdate))
        self.write_clients_to_file(clients)
        self.__previous.append(copy)

    def delete_client(self, index):
        clients = self.read_clients_from_file()
        copy = clients[:]
        if 0 <= index < len(clients):
            clients.pop(index)
            self.write_clients_to_file(clients)
            self.__previous.append(copy)

    def modify_client(self, number, name, cnp, birthdate):
        clients = self.read_clients_from_file()
        copy = clients[:]
        n=int(number)
        if 0 <= n <= len(clients):
            clients[n-1].set_name(name)
            clients[n-1].set_cnp(cnp)
            clients[n-1].set_birthdate(birthdate)
            self.write_clients_to_file(clients)
            self.__previous.append(copy)
            return clients[n-1]
        return None

    def find_client(self, id):
        clients = self.read_clients_from_file()
        index=int(id)
        for client in clients:
            if int(client.get_id()) == index:
                return client.get_name()
        return None

    def undo(self):
        if self.__previous:
            before = self.__previous.pop()
            self.write_clients_to_file(before)
        else:
            return None

    def print_clients(self):
        return self.read_clients_from_file()
