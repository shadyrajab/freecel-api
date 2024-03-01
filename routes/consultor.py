from typing import Optional
from utils.functions import create_client, jsonfy
from models.consultor import Consultor

def get_consultores():
    client = create_client()
    return jsonfy(client.get_consultores(to_dataframe = True))

def add_consultor_to_db(consultor: Consultor):
    client = create_client()
    client.add_consultor(consultor)

class Consultor:
    def __init__(self, nome: str, ano: Optional[int] = None, mes: Optional[str] = None, display_vendas: Optional[bool] = None):
        consultor = create_client().Consultor(nome)

        self.nome = consultor.name
        self.receita =  consultor.receita(ano, mes)
        self.volume =  consultor.volume(ano, mes)
        self.clientes = consultor.clientes(ano, mes)
        self.receita_media =  consultor.receita_media(ano, mes)
        self.volume_media =  consultor.volume_media(ano, mes)
        self.clientes_media = consultor.clientes_media(ano, mes)
        self.ticket_medio = consultor.ticket_medio(ano, mes)
        self.delta_receita = consultor.delta_receita(ano, mes) if ano else 0
        self.delta_volume = consultor.delta_volume(ano, mes) if ano else 0
        self.delta_clientes = consultor.delta_clientes(ano, mes) if ano else 0
        self.delta_ticket_medio = consultor.delta_ticket_medio(ano, mes) if ano else 0
        self.delta_receita = consultor.delta_receita(ano, mes) if ano else 0
        if display_vendas:
            self.vendas = jsonfy(consultor.filter_by(ano, mes))
            
        self.dates = consultor.dates
        self.ranking_planos = jsonfy(consultor.ranking_planos(ano, mes))
        self.ranking_produtos = jsonfy(consultor.ranking_produtos(ano, mes))