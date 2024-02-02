from structures.consultores.consultor import Consultor
from structures.rankings.ranking import Rankings
from dataframe.dataframe import DataFrame
import pandas as pd
    
class Client(
    DataFrame
):
    def __init__(self, host, database, user, password):
        super().__init__(
            host,
            database,
            user,
            password
        )

    def Consultor(self, nome):
        return Consultor(nome)
    
    def Ranking(self):
        return Rankings()

    def quantidade_de_vendas(self, ano: int = None, mes: str = None) -> int:

        """
            Retorna a quantidade de vendas em um determinado período. Função costuma ser utilizada
            como parâmetro para o cálculo de certas médias

            #### Parâmetros 

            ano : int | None
                Parâmetro opcional, caso informado, retornará a quantidade do ano inteiro

            mes : str | None
                Parâmetro opcional, caso informado, retornará a quantidade daquele mês. O parâmetro 
                ``ano`` é obrigatório caso ``mes`` seja passado. 
        """

        return self.filter_by(ano, mes).dataframe.shape[0]

    def receita_total(self, ano: int = None, mes: str = None) -> int:

        """
            Retorna a receita total de vendas em um determinado período.

            #### Parâmetros 

            ano : int | None
                Parâmetro opcional, caso informado, retornará a receita do ano inteiro

            mes : str | None
                Parâmetro opcional, caso informado, retornará a receita daquele mês. O parâmetro 
                ``ano`` é obrigatório caso ``mes`` seja passado. 
        """

        return self.filter_by(ano, mes).dataframe['VALOR ACUMULADO'].sum()
    
    def ticket_medio(self, ano: int = None, mes: str = None) -> int:

        """
            Retorna o ticket médio da empresa em um determinado período.

            #### Parâmetros 

            ano : int | None
                Parâmetro opcional, caso informado, retornará o ticket médio do ano inteiro

            mes : str | None
                Parâmetro opcional, caso informado, retornará o ticket médio daquele mês. O parâmetro 
                ``ano`` é obrigatório caso ``mes`` seja passado. 
        """

        return self.receita_total(ano, mes) / self.quantidade_de_vendas(ano, mes)

    def consultor_do_mes(self, ano: int = None, mes: str = None) -> Consultor:

        """
            Retorna a instância do ``Consultor`` que possuiu a maior receita em um determinado período.

            #### Parâmetros 

            ano : int | None
                Parâmetro opcional, caso informado, retornará o consultor que mais vendeu no ano inteiro

            mes : str | None
                Parâmetro opcional, caso informado, retornará o consultor que mais vendeu naquele mês 
                O parâmetro ``ano`` é obrigatório caso ``mes`` seja passado. 
        """

        dataframe: pd.DataFrame = self.filter_by(ano, mes).dataframe
        consultor_nome: str = dataframe.groupby('CONSULTOR')['VALOR ACUMULADO'].sum().idxmax()
        consultor_do_mes: Consultor = self.Consultor(consultor_nome)

        return consultor_do_mes
        
    def receita_media_diaria(self, ano: int = None, mes: str = None) -> int:

        """
            Retorna a receita média diária de vendas em um determinado período.

            #### Parâmetros 

            ano : int | None
                Parâmetro opcional, caso informado, retornará a media do ano inteiro

            mes : str | None
                Parâmetro opcional, caso informado, retornará a media daquele mês. O parâmetro 
                ``ano`` é obrigatório caso ``mes`` seja passado. 
        """

        return self.receita_total(ano, mes) / 22
    
    def media_por_consultor(self, ano: int = None, mes: str = None) -> int:

        """
            Retorna a receita média vendida por cada consultor em um determinado período.

            #### Parâmetros 

            ano : int | None
                Parâmetro opcional, caso informado, retornará a media do ano inteiro

            mes : str | None
                Parâmetro opcional, caso informado, retornará a media daquele mês. O parâmetro 
                ``ano`` é obrigatório caso ``mes`` seja passado. 
        """

        dataframe: pd.DataFrame = self.filter_by(ano, mes).dataframe
        consultores: int = dataframe['CONSULTOR'].nunique() # -> Quantidade de consultores
        media_por_consultor: int = self.receita_total(ano, mes) / consultores

        return media_por_consultor

    