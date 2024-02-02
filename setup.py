from client.client import Client

client = Client(
    host='localhost', 
    database='freecel', 
    user='postgres', 
    password='@sH^2004_'
)


flavio_ticket_medio = client.Consultor('FLAVIO HENRIQUE').ticket_medio

print(flavio_ticket_medio)

"""
    Client -> {
        CONSULTORES,
        ESCRITORIO,
        PRODUTOS,
        RANKINGS
    } -> {
        DATAFRAME -> {
            CONNECTION
        }
    }
"""