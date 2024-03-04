from typing import Optional
from utils.functions import create_client

class Freecel:
    def __init__(self, ano: Optional[int] = None, mes: Optional[str] = None):
        self.freecel = create_client().Freecel(ano, mes)

    @property
    def receita(self):
        return self.freecel.receita
    
    @property
    def volume(self):
        return self.freecel.volume
    
    @property
    def clientes(self):
        return self.freecel.clientes
    
    @property
    def ticket_medio(self):
        return self.freecel.ticket_medio
    
    @property
    def receita_media(self):
        return self.freecel.receita_media
    
    @property
    def media_consultor_geral(self):
        return self.freecel.media_consultor_geral
    
    @property
    def media_consultor_altas(self):
        return self.freecel.media_consultor_altas
    
    @property
    def media_consultor_migracao(self):
        return self.freecel.media_consultor_migracao
    
    @property
    def media_consultor_fixa(self):
        return self.freecel.media_consultor_fixa
    
    @property
    def media_consultor_avancada(self):
        return self.freecel.media_consultor_avancada
    
    @property
    def media_consultor_vvn(self):
        return self.freecel.media_consultor_vvn
    
    @property
    def delta_receita(self):
        return self.freecel.delta_receita
    
    @property
    def delta_volume(self):
        return self.freecel.delta_volume
    
    @property
    def delta_clientes(self):
        return self.freecel.delta_clientes
    
    @property
    def delta_ticket_medio(self):
        return self.freecel.delta_ticket_medio
    
    @property
    def delta_receita_media(self):
        return self.freecel.delta_receita_media
    
    @property
    def delta_media_consultor_geral(self):
        return self.freecel.delta_media_consultor_geral
    
    @property
    def ufs(self):
        return self.freecel.ufs
    
    @property
    def dates(self):
        return self.freecel.dates
    