from typing import Optional
from utils.functions import create_client

class Stats:
    def __init__(self, ano: Optional[int] = None, mes: Optional[str] = None):
        freecel = create_client().Freecel()

        self.receita = freecel.receita(ano, mes)
        self.volume = freecel.volume(ano, mes)
        self.clientes = freecel.clientes(ano, mes)
        self.ticket_medio = freecel.ticket_medio(ano, mes)
        self.receita_media_diaria = freecel.receita_media(ano, mes)
        self.media_por_consultor_geral = freecel.media_por_consultor(ano, mes)
        self.media_por_consultor_altas = freecel.media_por_consultor(ano, mes, 'ALTAS')
        self.media_por_consultor_migracao = freecel.media_por_consultor(ano, mes, 'MIGRAÇÃO PRÉ-PÓS')
        self.media_por_consultor_fixa = freecel.media_por_consultor(ano, mes, 'FIXA')
        self.media_por_consultor_avancada = freecel.media_por_consultor(ano, mes, 'AVANÇADA')
        self.media_por_consultor_vvn = freecel.media_por_consultor(ano, mes, 'VVN')
        self.delta_receita = freecel.delta_receita(ano, mes) if ano else 0 
        self.delta_volume = freecel.delta_volume(ano, mes) if ano else 0
        self.delta_clientes = freecel.delta_clientes(ano, mes) if ano else 0
        self.delta_ticket_medio = freecel.delta_ticket_medio(ano, mes) if ano else 0
        self.delta_receita_media = freecel.delta_receita_media(ano, mes) if ano else 0
        self.delta_media_por_consultor = freecel.delta_media_por_consultor(ano, mes) if ano else 0
        self.ufs = freecel.ufs
        self.tipo_venda = freecel.tipo_venda
        self.dates = freecel.dates