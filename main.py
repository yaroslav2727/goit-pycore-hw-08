from colorama import Fore, Style, init
from contacts.address_book import AddressBook
from contacts.handlers import (
    add_contact, change_contact, show_phone,
    show_all, remove_phone, delete_contact,
    add_birthday, show_birthday, birthdays, 
    wipe_storage, show_help
)

init()

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    book = AddressBook.load_data()
    print(Fore.LIGHTGREEN_EX + "Welcome to the assistant bot!" + Style.RESET_ALL + "\nType 'help' to see available commands.")
    
    while True:
        user_input = input(Style.DIM + "Enter a command: " + Style.RESET_ALL).strip()
        if not user_input:
            continue
            
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            book.save_data()
            print(Fore.LIGHTRED_EX + "Good bye!" + Style.RESET_ALL)
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "remove":
            print(remove_phone(args, book))
        elif command == "delete":
            print(delete_contact(args, book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))
        elif command == "wipe-storage":
            print(wipe_storage(args, book))
        elif command == "help":
            print(show_help(args, book))
        else:
            print(Fore.RED + "Invalid command." + Style.RESET_ALL + "\nType 'help' to see available commands.")
            # print("Type 'help' to see available commands.")

if __name__ == "__main__":
    main()