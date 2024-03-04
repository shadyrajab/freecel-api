from typing import Optional
from utils.functions import jsonfy
from client.client import Client

class Consultor:
    def __init__(self, client: Client, nome: str, ano: Optional[int] = None, mes: Optional[str] = None, display_vendas: Optional[bool] = None):
        self.consultor = client.Consultor(nome, ano, mes)
        self.display_vendas = display_vendas
    
    @property
    def nome(self) -> str:
        return str(self.consultor.nome)
    
    @property
    def receita(self) -> float:
        return float(self.consultor.receita)
    
    @property
    def volume(self) -> int:
        return int(self.consultor.volume)
    
    @property
    def clientes(self) -> int:
        return int(self.consultor.clientes)
    
    @property
    def receita_media(self) -> float:
        return float(self.consultor.receita_media)
    
    @property
    def volume_media(self) -> float:
        return float(self.consultor.volume_media)
    
    @property
    def clientes_media(self) -> float:
        return float(self.consultor.clientes_media)
    
    @property
    def ticket_medio(self) -> float:
        return float(self.consultor.ticket_medio)
    
    # @property
    # def delta_receita(self) -> float:
    #     return float(self.consultor.delta_receita)
    
    # @property
    # def delta_volume(self) -> float:
    #     return float(self.consultor.delta_volume)
    
    # @property
    # def delta_clientes(self) -> float:
    #     return float(self.consultor.del)
    
    # @property
    # def delta_ticket_medio(self) -> float:
    #     return float(self.consultor.delta_ticket_medio)
    
    @property
    def vendas(self):
        if not self.display_vendas:
            return {}
        
        return jsonfy(self.consultor.dataframe)
    
    # @property
    # def dates(self):
    #     return jsonfy(self.consultor.dates)
    
    @property
    def ranking_planos(self):
        return jsonfy(self.consultor.ranking_planos)
    
    @property
    def ranking_produtos(self):
        return jsonfy(self.consultor.ranking_produtos)
    
    def to_json(self):
        data = {}
        for attr_name, attr_value in vars(Consultor).items():
            if isinstance(attr_value, property):
                data[attr_name] = getattr(self, attr_name)

        return data
    


