from os import getenv

from dotenv import load_dotenv

load_dotenv()

HOST = getenv("host")
DATABASE = getenv("database")
USER = getenv("user")
PASSWORD = getenv("password")
TOKENEMPRESAS = getenv("tokenEmpresas")

PAYLOAD = {
    "action": "login",
    "user": getenv("userGestao"),
    "password": getenv("passwordGestao"),
}
