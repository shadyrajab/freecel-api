from typing import Optional
from utils.functions import create_client, jsonfy

class Consultor:
    def __init__(self, nome: str, ano: Optional[int] = None, mes: Optional[str] = None, display_vendas: Optional[bool] = None):
        self.consultor = create_client.Consultor(nome, ano, mes)
        self.display_vendas = display_vendas
    
    @property
    def nome(self):
        return self.consultor.nome
    
    @property
    def receita(self):
        return self.consultor.receita
    
    @property
    def volume(self):
        return self.consultor.volume
    
    @property
    def clientes(self):
        return self.consultor.clientes
    
    @property
    def receita_media(self):
        return self.consultor.receita_media
    
    @property
    def volume_media(self):
        return self.consultor.volume_media
    
    @property
    def clientes_media(self):
        return self.consultor.clientes_media
    
    @property
    def ticket_medio(self):
        return self.consultor.ticket_medio
    
    @property
    def delta_receita(self):
        return self.consultor.delta_receita
    
    @property
    def delta_volume(self):
        return self.consultor.delta_volume
    
    @property
    def delta_clientes(self):
        return self.consultor.delta_clientes
    
    @property
    def delta_ticket_medio(self):
        return self.consultor.delta_ticket_medio
    
    @property
    def vendas(self):
        if not self.display_vendas:
            return {}
        
        return jsonfy(self.consultor.dataframe)
    
    @property
    def dates(self):
        return self.consultor.dates
    
    @property
    def ranking_planos(self):
        return self.consultor.ranking_planos
    
    @property
    def ranking_produtos(self):
        return self.consultor.ranking_produtos