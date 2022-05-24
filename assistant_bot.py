exit_commands = ('good_bye', 'close', 'exit')
contacts = {}


def input_error(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            f_name = func.__name__
            if f_name in ('hello', 'show_all_phones'):
                print("ERROR: This command has to be written without arguments!")
            if f_name in ('add_phone', 'change_phone'):
                print("ERROR: This command needs 2 arguments: 'name' and 'phone'!")
            if f_name == 'show_phone':
                print("ERROR: This command needs 1 arguments: 'name'!")

    return wrapper


@input_error
def hello() -> None:
    print("Hello! How can I help you?")


@input_error
def add_phone(name: str, phone: str) -> None:
    if name in contacts.keys():
        print(f"Name '{name}' is already in contacts!")
        print("Try another name or change existing contact")
        return

    contacts.update({name: phone})
    print(f'Contact was added successfully!')


@input_error
def change_phone(name: str, phone: str):
    if name not in contacts.keys():
        print(f"There is no contact with name {name}")
        return

    contacts.update({name: phone})
    print(f'Contact was updated successfully!')


@input_error
def show_phone(name: str) -> None:
    if name not in contacts.keys():
        print(f"There is no contact with name {name}")
        return

    print(contacts.get(name))


@input_error
def show_all_phones() -> None:
    if not contacts:
        print("There are no contacts to show yet...")
        return

    for name, phone in contacts.items():
        print(name, phone)


# @func_decorator
def choose_command(cmd: str):
    if cmd == 'hello':
        return hello
    if cmd == 'add':
        return add_phone
    if cmd == 'change':
        return change_phone
    if cmd == 'phone':
        return show_phone
    if cmd == 'show':
        return show_all_phones
    else:
        print('Unknown command')
        return None


def handle_command(cmd: str):
    cmd = cmd.strip().split(' ')  # apply strip() as well to exclude spaces at the ends
    func = choose_command(cmd[0].lower())
    if func:
        func(*cmd[1:]) if len(cmd) > 1 else func()  # else part to take into account hello() and show()


def main():
    while True:
        command = None

        # Check if command is not empty
        while not command:
            command = input('Enter command: ')

        if command in exit_commands:
            break

        handle_command(command)
        print()


if __name__ == '__main__':
    main()
