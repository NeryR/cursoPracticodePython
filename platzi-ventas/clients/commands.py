import click

@click.group()
def clients():
    """Manages the clients lifecycle"""


@clients.command()
@click.pass_context
def create(ctx, name, company, email, position):
    """Create new client"""
    pass


@clients.command()
@click.pass_context
def  list(ctx):
    """List clients"""
    pass


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
