from messages import MESSAGES
from decorators import input_error
from utils import parse_input


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return MESSAGES["add_success"]


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return MESSAGES["change_success"]
    else:
        return MESSAGES["contact_not_found"]


@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return MESSAGES["phone_found"](name, contacts[name])
    else:
        return MESSAGES["contact_not_found"]


@input_error
def show_all(contacts):
    if not contacts:
        return MESSAGES["all_empty"]
    result = [MESSAGES["all_header"]]
    for name, phone in contacts.items():
        result.append(MESSAGES["all_entry"](name, phone))
    return "\n".join(result)


@input_error
def show_help():
    return MESSAGES["help"]


def main():
    contacts = {}
    print(MESSAGES["welcome"])

    while True:
        user_input = input(MESSAGES["prompt"])
        command, args = parse_input(user_input)

        if not command:
            continue

        if command in ["close", "exit"]:
            print(MESSAGES["goodbye"])
            break
        elif command == "hello":
            print(MESSAGES["greeting"])
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command in ["help", "-h"]:
            print(show_help())
        else:
            print(MESSAGES["invalid"])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(MESSAGES["goodbye"])
