from dataclasses import dataclass, asdict
import json
from contextlib import contextmanager

@dataclass
class User:
    user_id: int
    name: str
    surname: str
    pesel: str

    @contextmanager
    def open_file(self, file_path, mode):
        file = open(file_path, mode)
        try:
            yield file
        finally:
            file.close()

    def write_to_json_file(self, file_path):
        with self.open_file(file_path, 'w') as file:
            json.dump(asdict(self), file, indent=4)

    def load_from_json_file(self, file_path):
        with self.open_file(file_path, 'r') as file:
            data = json.load(file)
        self.user_id = data["user_id"]
        self.name = data["name"]
        self.surname = data["surname"]
        self.pesel = data["pesel"]

    def __str__(self):
        return f"{self.name} {self.surname}"

# Przykład użycia
u = User(1, 'Aleksiej', 'Siemionow', '111234151')

print(u.user_id)
print(u)

print(
    f"id: {u.user_id}\nName: {u.name}\nSurname: {u.surname}\nPesel: {u.pesel}"
)

u.write_to_json_file('/home/alex/projects/python_labs/lab_3/user.json')
print("User data saved.")

u.load_from_json_file('/home/alex/projects/python_labs/lab_3/user.json')
print("User data loaded:", u)
