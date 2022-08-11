clients = 'Pablo, Ricardo, '

def create_client(client_name):
    # Con el comando global se puede acceder a las variables externas dentro de una función
    global clients
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else: 
        print('Client already is in the client\' list')


def list_clients():
    global clients
    print(clients)


def update_client(client_name, updated_client_name):
    global clients
    if client_name  in clients:
        clients = clients.replace(client_name + ', ', updated_client_name + ', ')
    else:
        print('Client is not in clients list')


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ', ', '')
    else:
        print('Client is not in clients list')


def _add_comma():
    global clients
    clients += ", "


def _print_welcome():
    print('Welcome to Platzi Ventas')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C] Create client')
    print('[U] Update client')
    print('[D] Delete client')

def _get_client_name():
    return input('What\'s the client name? ')


if __name__ == "__main__":
    _print_welcome()
    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What\'s the updated client name? ')
        update_client(client_name, updated_client_name)
        list_clients()
    else:
        print('Invalid command')
