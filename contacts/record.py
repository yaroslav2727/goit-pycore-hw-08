from colorama import Fore, Style
from .fields import Name, Phone, Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        if phone_obj not in self.phones:
            self.phones.append(phone_obj)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                self.phones.remove(p)
                self.add_phone(new_phone)
                return
        raise ValueError("Phone not found")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        name_str = f"{Fore.GREEN}{self.name.value}{Style.RESET_ALL}"
        phones_str = '; '.join(f"{Fore.YELLOW}{p.value}{Style.RESET_ALL}" for p in self.phones)
        birthday_str = ""
        if self.birthday:
            birthday_str = f", birthday: {Fore.CYAN}{self.birthday}{Style.RESET_ALL}"
        return f"Contact name: {name_str}, phones: {phones_str}{birthday_str}"
