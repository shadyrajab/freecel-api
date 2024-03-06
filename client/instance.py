from client.client import Client
from utils.variables import HOST, DATABASE, USER, PASSWORD

def get_client():
    client = Client(
        HOST,
        DATABASE,
        USER,
        PASSWORD
    )

    return client