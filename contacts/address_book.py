from collections import UserDict
from datetime import datetime, timedelta
import pickle

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.today()
        upcoming_birthdays = []
        
        for name, record in self.data.items():
            if record.birthday is None:
                continue
                
            birthday = datetime.strptime(record.birthday.value, '%d.%m.%Y')
            birthday_this_year = birthday.replace(year=today.year)
            
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            
            days_until_birthday = (birthday_this_year - today).days
            
            if 0 <= days_until_birthday <= 7:
                congratulation_date = birthday_this_year
                
                # Якщо припадає на вихідний, ставимо на наступний понеділок
                if congratulation_date.weekday() >= 5:  # Субота (5) або Неділя (6)
                    congratulation_date += timedelta(days=(7 - congratulation_date.weekday()))
                
                upcoming_birthdays.append({
                    'name': name,
                    'congratulation_date': congratulation_date.strftime('%d.%m.%Y')
                })
        
        return upcoming_birthdays
    
    def save_data(book, filename="addressbook.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(book, f)

    def load_data(filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return AddressBook()