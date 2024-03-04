from utils.functions import create_client, jsonfy
from typing import Optional

class Rankings:
    def __init__(self, ano: Optional[int] = None, mes: Optional[str] = None):
        self.ranking = create_client().Ranking(ano, mes)

    @property
    def consultores(self):
        return jsonfy(self.ranking.consultores)
    
    @property
    def produtos(self):
        return jsonfy(self.ranking.produtos)
    
    @property
    def planos(self):
        return jsonfy(self.ranking.planos)
    
    @property
    def fixa(self):
        return jsonfy(self.ranking.produtos)
    
    @property
    def avancada(self):
        return jsonfy(self.ranking.avancada)

    @property
    def vvn(self):
        return jsonfy(self.ranking.vvn)
    
    @property
    def migracao(self):
        return jsonfy(self.ranking.migracao)
    
    @property
    def altas(self):
        return jsonfy(self.ranking.altas)