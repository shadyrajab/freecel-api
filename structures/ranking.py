import pandas as pd
from typing import Optional

from database.dataframe import DataFrame

class Rankings:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def filter_by(self, ano: Optional[int] = None, mes: Optional[str] = None, tipo: Optional[str] = None):
        return DataFrame.__filter_by__(dataframe = self.dataframe, ano = ano, mes = mes, tipo = tipo)
    
    def produtos(self, ano: Optional[int] = None, mes: Optional[str] = None):
        """ 
            Retorna um ``DataFrame`` com o ranking dos produtos que mais venderam em um determinado 
            período.

            Parâmetros:
            -----------
            ano : int | None
                Parâmetro opcional para filtrar as vendas por base no ano. Se fornecido, o ranking
                será para esse ano. 

            mes : str | None
                Parâmetro opcional para filtrar as vendas por base no mês. Se fornecido, o ranking 
                será para esse mês. O parâmetro ano deve ser fornecido caso o mês seja especificado.

            Retorna:
            -----------
            pd.DataFrame
                Um DataFrame contendo o ranking dos produtos com base na quantidade total de vendas.
         """
        quantidade_de_vendas = self.filter_by(ano, mes)['tipo'].value_counts().reset_index()
        quantidade_de_vendas.columns = ['tipo', 'quantidade_de_vendas']

        ranking_produtos = self.filter_by(ano, mes).groupby('tipo', as_index = False).sum(numeric_only = True)
        ranking_produtos.drop(['ano', 'valor_do_plano', 'id'], axis = 1, inplace = True)

        return pd.merge(ranking_produtos, quantidade_de_vendas, on = 'tipo')

    def consultores(self, ano: Optional[int] = None, mes: Optional[str] = None, tipo: Optional[str] = None) -> pd.DataFrame:
        """ 
            Retorna um ``DataFrame`` com o ranking dos consultores que mais venderam em um determinado 
            período.

            Parâmetros:
            -----------
            ano : int | None
                Parâmetro opcional para filtrar as vendas por base no ano. Se fornecido, o ranking
                será para esse ano. 

            mes : str | None
                Parâmetro opcional para filtrar as vendas por base no mês. Se fornecido, o ranking 
                será para esse mês. O parâmetro ano deve ser fornecido caso o mês seja especificado.

            tipo: str | None
                Parâmetro opcional para gerar o ranking baseado no tipo de venda. Se fornecido, será
                gerado um ranking para um tipo de venda específico 
            """
        
        if tipo and tipo not in {'ALTAS', 'FIXA', 'AVANÇADA', 'VVN', 'MIGRAÇÃO PRÉ-PÓS'}:
            raise ValueError("O tipo de venda deve ser {'ALTAS', 'FIXA' | 'AVANÇADA' | 'VVN' | 'MIGRAÇÃO PRÉ-PÓS'}")
        
        quantidade_de_vendas = self.filter_by(ano, mes, tipo)['consultor'].value_counts().reset_index()
        quantidade_de_vendas.columns = ['consultor', 'quantidade_de_vendas']
        
        ranking_consultores = self.filter_by(ano, mes, tipo).groupby('consultor', as_index = False).sum(numeric_only = True)
        ranking_consultores.drop(['ano', 'valor_do_plano', 'id'], axis = 1, inplace = True)

        return pd.merge(ranking_consultores, quantidade_de_vendas, on = 'consultor')

