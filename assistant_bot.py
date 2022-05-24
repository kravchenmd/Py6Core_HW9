
exit_commands = ['good_bye', 'close', 'exit']
contacts = []

def func_decorator(func):
    def wrapper(*args):
        print(args)
        if len(args) > 1:
            func(*args[1:])
            return
        func()
    return wrapper

@func_decorator
def hello(*args) -> None:
    print("Hello! How can I help you?")

@func_decorator
def add_phone(name: str, phone: str) -> None:
    contacts.append({'name': name, 'phone': phone})
    print('End add')

@func_decorator
def change_phone(name: str, phone: str) -> bool:
    for contact in contacts:
        if contact.get('name') == name:
            contact['phone'] = phone
        return True
    return False

@func_decorator
def show_phone(name: str) -> None:
    for contact in contacts:
        if contact.get('name') == name:
            print(contact.get('phone'))

@func_decorator
def show_all_phones() -> None:
    for contact in contacts:
        print(contact.get('name'), contact.get('phone'))

# @func_decorator
def choose_command(command: str):
    if command == 'hello':
        return hello
    if command == 'add':
        return add_phone
    if command == 'change':
        return change_phone
    if command == 'show':
        return show_phone
    else:
        print('Unknown command')
        return None


while True:
    command = None
    # Check if command is not empty
    while not command:
        command = input('Enter command: ')

    command = command.split(' ')
    func = choose_command(command[0].lower())

    if func:
        func(*command)

    if command in exit_commands:
        break

    print(contacts)


