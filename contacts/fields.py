from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Phone must be a string")
        if not value.isdigit():
            raise ValueError("Phone must contain only digits")
        if len(value) != 10:
            raise ValueError("Phone must be 10 digits long")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.date = datetime.strptime(value, '%d.%m.%Y')
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self.date.strftime('%d.%m.%Y')