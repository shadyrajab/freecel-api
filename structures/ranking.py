import pandas as pd
from typing import Optional

from dataframe.dataframe import DataFrame

class Rankings:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def filter_by(self, ano: Optional[int] = None, mes: Optional[str] = None, tipo: Optional[str] = None):
        return DataFrame.__filter_by__(self.dataframe, ano, mes, tipo)
    
    def ranking_produtos(self, ano: Optional[int] = None, mes: Optional[str] = None):
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
        
        ranking_produtos = self.filter_by(ano, mes).groupby('TIPO', as_index = False).sum(numeric_only = True)
        ranking_produtos.drop(['ANO', 'VALOR DO PLANO'], axis = 1, inplace = True)

        return ranking_produtos

    def ranking_consultores(self, ano: Optional[int] = None, mes: Optional[str] = None, tipo: Optional[int] = None) -> pd.DataFrame:
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

            Retorna:
            -----------
            pd.DataFrame
                Um DataFrame contendo o ranking dos consultores com base na quantidade total de vendas.
         """
        
        if tipo and tipo not in {'FIXA', 'AVANÇADA', 'VVN', 'MIGRAÇÃO PRÉ-PÓS'}:
            raise ValueError("O tipo de venda deve ser {'ALTAS', 'FIXA' | 'AVANÇADA' | 'VVN' | 'MIGRAÇÃO PRÉ-PÓS'}")
        
        ranking_consultores = self.filter_by(ano, mes, tipo).groupby('CONSULTOR', as_index = False).sum(numeric_only = True)
        ranking_consultores.drop(['ANO', 'VALOR DO PLANO'], axis = 1, inplace = True)

        return ranking_consultores

