import pandas as pd
from typing import Optional

from database.dataframe import DataFrame

class Rankings:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def filter_by(self, ano: Optional[int] = None, mes: Optional[str] = None, tipo: Optional[str] = None):
        return DataFrame.__filter_by__(dataframe = self.dataframe, ano = ano, mes = mes, tipo = tipo)
    
    def planos(self, ano: Optional[int] = None, mes: Optional[str] = None):
        quantidade_de_vendas = self.filter_by(ano, mes)['plano'].value_counts().reset_index()
        quantidade_de_vendas.columns = ['plano', 'quantidade_de_vendas']

        ranking_planos = self.filter_by(ano, mes).groupby('plano', as_index = False).sum(numeric_only = True)
        ranking_planos.drop(['ano', 'valor_do_plano', 'id'], axis = 1, inplace = True)

        return pd.merge(ranking_planos, quantidade_de_vendas, on = 'plano')
    
    def produtos(self, ano: Optional[int] = None, mes: Optional[str] = None):
        quantidade_de_vendas = self.filter_by(ano, mes)['tipo'].value_counts().reset_index()
        quantidade_de_vendas.columns = ['tipo', 'quantidade_de_vendas']

        ranking_produtos = self.filter_by(ano, mes).groupby('tipo', as_index = False).sum(numeric_only = True)
        ranking_produtos.drop(['ano', 'valor_do_plano', 'id'], axis = 1, inplace = True)

        return pd.merge(ranking_produtos, quantidade_de_vendas, on = 'tipo')

    def consultores(self, ano: Optional[int] = None, mes: Optional[str] = None, tipo: Optional[str] = None) -> pd.DataFrame:
        if tipo and tipo not in {'ALTAS', 'FIXA', 'AVANÇADA', 'VVN', 'MIGRAÇÃO PRÉ-PÓS'}:
            raise ValueError("O tipo de venda deve ser {'ALTAS', 'FIXA' | 'AVANÇADA' | 'VVN' | 'MIGRAÇÃO PRÉ-PÓS'}")
        
        quantidade_de_vendas = self.filter_by(ano, mes, tipo)['consultor'].value_counts().reset_index()
        quantidade_de_vendas.columns = ['consultor', 'quantidade_de_vendas']
        
        ranking_consultores = self.filter_by(ano, mes, tipo).groupby('consultor', as_index = False).sum(numeric_only = True)
        ranking_consultores.drop(['ano', 'valor_do_plano', 'id'], axis = 1, inplace = True)

        return pd.merge(ranking_consultores, quantidade_de_vendas, on = 'consultor')

