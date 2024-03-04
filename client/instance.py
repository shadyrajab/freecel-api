from client.client import Client
from utils.variables import HOST, DATABASE, USER, PASSWORD

client = Client(
    HOST,
    DATABASE,
    USER,
    PASSWORD
)