from utils.functions import create_client, jsonfy
from typing import Optional

class Rankings:
    def __init__(self, ano: Optional[int] = None, mes: Optional[str] = None):
        client = create_client()
        rankings = client.Ranking()

        self.ranking_consultores = jsonfy(rankings.ranking_consultores(ano, mes))
        self.ranking_produtos = jsonfy(rankings.ranking_produtos(ano, mes))
        self.ranking_fixa = jsonfy(rankings.ranking_consultores(ano, mes, tipo = 'FIXA'))
        self.ranking_avancada = jsonfy(rankings.ranking_consultores(ano, mes, tipo = 'AVANÇADA'))
        self.ranking_vvn = jsonfy(rankings.ranking_consultores(ano, mes, tipo = 'VVN'))
        self.ranking_migracao = jsonfy(rankings.ranking_consultores(ano, mes, tipo  = 'MIGRAÇÃO PRÉ-PÓS'))
        self.ranking_altas = jsonfy(rankings.ranking_consultores(ano, mes, tipo = 'ALTAS'))
        self.ranking_planos = jsonfy(rankings.ranking_planos(ano, mes))