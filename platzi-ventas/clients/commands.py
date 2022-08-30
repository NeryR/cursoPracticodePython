import click
from tabulate import tabulate

from clients.services import ClientService
from clients.models import Client

@click.group()
def clients():
    """Manages the clients lifecycle"""


@clients.command()
@click.option('-n', '--name', type=str, prompt=True, help='The client name')
@click.option('-c', '--company', type=str, prompt=True, help='The client company')
@click.option('-e', '--email', type=str, prompt=True, help='The client email')
@click.option('-p', '--position', type=str, prompt=True, help='The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Create new client"""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)


@clients.command()
@click.pass_context
def  list(ctx):
    """List clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    clients_list = client_service.list_clients()

    headers = [field.capitalize() for field in Client.schema()]
    table = []

    for client in clients_list:
        table.append(
            [client['name'],
            client['company'],
            client['email'],
            client['position'],
            client['uid']]
        )
    print(tabulate(table, headers))


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Update client"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Delete client"""
    pass


all = clients
