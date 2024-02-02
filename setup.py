from client.client import Client

client = Client(
    host='localhost', 
    database='freecel', 
    user='postgres', 
    password='@sH^2004_'
)

client.consultor_do_mes(2023, 'JAN')

"""
    Client -> {
        CONSULTORES[PRIVATE_METHODS],
        ESCRITORIO[PRIVATE_METHODS],
        PRODUTOS[PRIVATE_METHODS],
        RANKINGS[PRIVATE_METHODS]
    } -> {
        DATAFRAME -> {
            CONNECTION
        }
    }
"""