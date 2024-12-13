import json
from contextlib import contextmanager


class User:
    def __init__(self, user_id, name, surname, pesel):
        self.user_id = user_id
        self.__name = name
        self.__surname = surname
        self.__pesel = pesel

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def pesel(self):
        return self.__pesel

    @pesel.setter
    def pesel(self, pesel):
        self.__pesel = pesel

    @contextmanager
    def open_file(self, file_path, mode):
        file = open(file_path, mode)
        try:
            yield file
        finally:
            file.close()

    def write_to_json_file(self, file_path):
        data = {
            "user_id": self.__user_id,
            "name": self.__name,
            "surname": self.__surname,
            "pesel": self.__pesel
        }

        with self.open_file(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def load_from_json_file(self, file_path):

        with open(file_path, 'r') as file:
            data = json.load(file)

        self.user_id = data.get("user_id")
        self.name = data.get("name")
        self.surname = data.get("surname")
        self.pesel = data.get("pesel")

    def load_from_json_file(self, file_path):

        with self.open_file(file_path, 'r') as file:
            data = json.load(file)

        self.__user_id = data.get("user_id")
        self.__name = data.get("name")
        self.__surname = data.get("surname")
        self.__pesel = data.get("pesel")

    def __str__(self):
        return self.__name + ' ' + self.__surname


u = User(1, 'Aleksiej', 'Siemionow', '111234151')

print(u.user_id)
print(u)

print('id: ' + str(u.user_id), 'Name: ' + u.name, 'Surname: ' + u.surname, 'Pesel ' + u.pesel, sep='\n')

u.write_to_json_file('/home/alex/projects/python_labs/lab_3/user.json')
print(u)

u.load_from_json_file('/home/alex/projects/python_labs/lab_3/user.json')
print(u)
