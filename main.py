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


def _add_comma():
    global clients
    clients += ", "


def _print_welcome():
    print('Welcome to Platzi Ventas')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C] Create client')
    print('[D] Delete client')


if __name__ == "__main__":
    _print_welcome()
    command = input()

    if command == 'C':
        client_name = input('What is the client name? ')
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    else:
        print('Invalid command')
