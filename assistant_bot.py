exit_commands = ('good_bye', 'close', 'exit')
contacts = {}


def func_decorator(func):
    def wrapper(*args):
        print(args)
        try:
            func(*args)
        except Exception as e:
            print(f"ERROR: {e}")

    return wrapper


@func_decorator
def hello() -> None:
    print("Hello! How can I help you?")


@func_decorator
def add_phone(name: str, phone: str) -> None:
    if name in contacts.keys():
        print(f"Name '{name}' is already in contacts!")
        print("Try another name or change existing contact")
        return

    contacts.update({name: phone})
    print(f'Contact was added successfully!')


@func_decorator
def change_phone(name: str, phone: str) -> bool:
    if name not in contacts.keys():
        print(f"There is no contact with name {name}")
        return

    contacts.update({name: phone})
    print(f'Contact was updated successfully!')


@func_decorator
def show_phone(name: str) -> None:
    if name not in contacts.keys():
        print(f"There is no contact with name {name}")
        return

    print(contacts.get(name))


@func_decorator
def show_all_phones() -> None:
    if not contacts:
        print("There are no contacts yet to show...")
        return

    for name, phone in contacts.items():
        print(name, phone)


# @func_decorator
def choose_command(command: str):
    if command == 'hello':
        return hello
    if command == 'add':
        return add_phone
    if command == 'change':
        return change_phone
    if command == 'phone':
        return show_phone
    if command == 'show':
        return show_all_phones
    else:
        print('Unknown command')
        return None


while True:
    command = None
    # Check if command is not empty
    while not command:
        command = input('Enter command: ')

    command = command.strip().split(' ')  # apply strip() as well to exclude spaces at the ends
    func = choose_command(command[0].lower())

    if func:
        # to take into account
        func(*command[1:]) if len(command) > 1 else func()  # else part to take into account hello() and show()

    if command in exit_commands:
        break
    # print(contacts)
    print()
