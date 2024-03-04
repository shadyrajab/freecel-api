from typing import Optional
from client.client import Client

class Freecel:
    def __init__(self, client: Client, ano: Optional[int] = None, mes: Optional[str] = None):
        self.freecel = client.Freecel(ano, mes)

    @property
    def receita(self) -> float:
        return float(self.freecel.receita)
    
    @property
    def volume(self) -> int:
        return int(self.freecel.volume)
    
    @property
    def clientes(self) -> int:
        return int(self.freecel.clientes)
    
    @property
    def ticket_medio(self) -> float:
        return float(self.freecel.ticket_medio)
    
    @property
    def receita_media(self) -> float:
        return float(self.freecel.receita_media)
    
    @property
    def media_consultor_geral(self) -> float:
        return float(self.freecel.media_consultor_geral)
    
    @property
    def media_consultor_altas(self) -> float:
        return float(self.freecel.media_consultor_altas)
    
    @property
    def media_consultor_migracao(self) -> float:
        return float(self.freecel.media_consultor_migracao)
    
    @property
    def media_consultor_fixa(self) -> float:
        return float(self.freecel.media_consultor_fixa)
    
    @property
    def media_consultor_avancada(self) -> float:
        return float(self.freecel.media_consultor_avancada)
    
    @property
    def media_consultor_vvn(self) -> float:
        return float(self.freecel.media_consultor_vvn)
    
    # @property
    # def delta_receita(self):
    #     return self.freecel.delta_receita
    
    # @property
    # def delta_volume(self):
    #     return self.freecel.delta_volume
    
    # @property
    # def delta_clientes(self):
    #     return self.freecel.delta_clientes
    
    # @property
    # def delta_ticket_medio(self):
    #     return self.freecel.delta_ticket_medio
    
    # @property
    # def delta_receita_media(self):
    #     return self.freecel.delta_receita_media
    
    # @property
    # def delta_media_consultor_geral(self):
    #     return self.freecel.delta_media_consultor_geral
    
    @property
    def ufs(self):
        return self.freecel.ufs
    
    # @property
    # def dates(self):
    #     return self.freecel.dates
    
    def to_json(self):
        data = {}
        for attr_name, attr_value in vars(Freecel).items():
            if isinstance(attr_value, property):
                data[attr_name] = getattr(self, attr_name)

        return data