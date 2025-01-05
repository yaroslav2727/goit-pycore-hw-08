from colorama import Fore, Style
from .record import Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e) if str(e) else "Enter a name and a valid phone number (10 digits)."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."
        except Exception as e:
            return f"Error: {e}"
    return inner

@input_error
def add_contact(args, book):
    if len(args) != 2:
        raise ValueError("Enter a name and a valid phone number (10 digits).")
    name, phone = args
    
    if not phone.isdigit() or len(phone) != 10:
        raise ValueError("Phone number must be 10 digits.")
        
    record = book.find(name)
    if record is None:
        record = Record(name)
        record.add_phone(phone)  # Only add record if phone is valid
        book.add_record(record)
    else:
        record.add_phone(phone)
    return "Contact added."

@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        raise KeyError
    
    record.edit_phone(old_phone, new_phone)
    return "Contact updated."

@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError
    return record

@input_error
def show_all(book):
    if not book.data:
        return "No contacts saved."
    return "\n".join(str(record) for record in book.data.values())

@input_error
def remove_phone(args, book):
    name, phone = args
    record = book.find(name)
    if record is None:
        raise KeyError
    record.remove_phone(phone)
    return "Phone removed."

@input_error
def delete_contact(args, book):
    name = args[0]
    if book.find(name) is None:
        raise KeyError
    book.delete(name)
    return "Contact deleted."

@input_error
def add_birthday(args, book):
    if len(args) != 2:
        raise ValueError("Enter both name and birthday (DD.MM.YYYY)")
    name, birthday = args
    record = book.find(name)
    if not record:
        raise KeyError("Contact not found")
    try:
        record.add_birthday(birthday)
        return "Birthday added."
    except ValueError as e:
        raise ValueError(str(e))

@input_error
def show_birthday(args, book):
    if len(args) != 1:
        raise ValueError("Enter a name")
    name = args[0]
    record = book.find(name)
    if not record:
        raise KeyError("Contact not found.")
    if not record.birthday:
        return "No birthday set for this contact."
    return f"{Fore.GREEN}{name}{Style.RESET_ALL}'s birthday: {Fore.CYAN}{record.birthday}{Style.RESET_ALL}"

@input_error
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No birthdays next week."
    result = []
    for item in upcoming:
        result.append(f"{Fore.GREEN}{item['name']}{Style.RESET_ALL}: {Fore.CYAN}{item['congratulation_date']}{Style.RESET_ALL}")
    return "Upcoming birthdays:\n" + "\n".join(result)

@input_error
def wipe_storage(args, book):
    confirmation = input(f"{Fore.RED}WARNING: This will delete all contacts. This operation cannot be undone.\nType 'YES' to confirm: {Style.RESET_ALL}")
    if confirmation.strip().upper() == "YES":
        book.data = {}
        book.save_data()
        return f"{Fore.LIGHTBLUE_EX}Storage wiped successfully.{Style.RESET_ALL}"
    return f"{Fore.LIGHTRED_EX}Operation cancelled.{Style.RESET_ALL}"

@input_error
def show_help(args, book):
    COMMANDS = {
    "hello": "Greet the bot",
    "add <name> <phone>": "Add new contact",
    "change <name> <old_phone> <new_phone>": "Change existing contact's phone",
    "phone <name>": "Show phone numbers for contact",
    "all": "Show all contacts",
    "remove <name> <phone>": "Remove phone from contact",
    "delete <name>": "Delete contact completely",
    "add-birthday <name> <date>": "Add birthday (or modify existing) for contact (date format: DD.MM.YYYY)",
    "show-birthday <name>": "Show birthday for contact",
    "birthdays": "Show upcoming birthdays (next work week)",
    "wipe-storage": "Delete all contacts (irreversible!)",
    "exit": "Close the program"
    }
    
    result = [f"{Fore.LIGHTBLUE_EX}Available commands:{Style.RESET_ALL}"]
    for cmd, desc in COMMANDS.items():
        result.append(f"{Fore.LIGHTCYAN_EX}{cmd}{Style.RESET_ALL}: {desc}")
    return "\n".join(result)