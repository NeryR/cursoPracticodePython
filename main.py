from pydoc import cli
import sys
from turtle import position


clients = [
    {
        'name': 'Pablo',
        'company': 'Google', 
        'email': 'pablo@google.com',
        'position': 'Software Engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook', 
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer',
    }


]

def create_client(client):
    # Con el comando global se puede acceder a las variables externas dentro de una función
    global clients
    if client not in clients:
        clients.append(client)
    else: 
        print('Client already is in the client\' list')


def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']
        ))


def update_client(client_id, updated_client):
    global clients
    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client not in client\'s list')


def delete_client(client_id):
    global clients
    for idx, client in enumerate(clients):
        if idx == client_id:    
            del clients[idx]
            break


def _print_welcome():
    print('Welcome to Platzi Ventas')
    print('*' * 100)
    print('What would you like to do today?')
    print('[C] Create client')
    print('[L] List clients')
    print('[U] Update client')
    print('[D] Delete client')
    print('[S] Search client')

def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}? '.format(field_name))

    return field

def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }
    return client

def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What\'s the client name? ')
        if client_name == 'exit':
            client_name = None
            break
    if not client_name:
            sys.exit()
    return client_name


if __name__ == "__main__":
    _print_welcome()
    command = input()
    command = command.upper()

    if command == 'C':
        client = _get_client_from_user()

        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'D':
        client_id = int(_get_client_field('id'))

        delete_client(client_id)
        list_clients()
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()

        update_client(client_id, updated_client)
        list_clients()
    elif command == "S":
        client_name = _get_client_field('name')
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print('The client {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')
