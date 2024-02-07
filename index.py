from fastapi import FastAPI
from dotenv import load_dotenv
from os import getenv
from client.client import Freecel

load_dotenv()

HOST = getenv('host')
DATABASE = getenv('database')
USER = getenv('user')
PASSWORD = getenv('password')

client = Freecel(
    host = HOST,
    database = DATABASE,
    user = USER,
    password = PASSWORD
)

receita = client.receita_total(2023, 'Janeiro')

print(receita)