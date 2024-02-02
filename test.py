from client.client import Client

client = Client(
    host='localhost', 
    database='freecel', 
    user='postgres', 
    password='@sH^2004_'
)

doidao = client.Consultor('FLAVIO HENRIQUE').receita_media_mensal
print(doidao)

"""

    Client -> {
        CONSULTORES -> { Private classes } {
        RANKINGS -> { Private classes }      DATAFRAME -> { 
        PRODUTOS -> { Private classes }            DATABASE }   
        ESCRITORIOS -> { Private classes }     }
    }
"""


"""
    Client -> {
        DATAFRAME -> {
            DATABASE
        }
    }

    self.consultor = Consultor(DATAFRAME)
    self.rankings = Rankings(DATAFRAME)

    A classe Client herda a classe Dataframe
    A classe Dataframe herda a classe Database

    A classe DATAFRAME é passada para as classes Consultor, Ranking, etc... diretamente, como forma
    de parâmetro 

"""