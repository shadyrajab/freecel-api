import pandas as pd
from database.dataframe import DataFrame
from datetime import datetime

from typing import Optional

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

class Consultor():
    def __init__(self, name, dataframe, filtro: Optional[list] = None):
        self.name = name
        self.dataframe = dataframe[
            (dataframe['consultor'] == name)
        ]

        if filtro:
            ano, mes = filtro
            self.dataframe = DataFrame.__filter_by__(self.dataframe, ano, mes)

    def filter_by(self, ano: Optional[int] = None, mes: Optional[str] = None):
        return DataFrame.__filter_by__(dataframe = self.dataframe, ano = ano , mes = mes)

    @property
    def dias_trabalhados(self) -> int:
        """
            Retorna quantos dias determinado consultor trabalhou aproximadamente. Valor é utilizado como
            métrica para o cálculo de certas médias

        """

        # Soma a quantidade de meses tabalhados com a quantidade de dias úteis de um mês
        dias_trabalhados = self.meses_trabalhados * 22
        
        return dias_trabalhados
    
    def quantidade_clientes(self, ano: Optional[int] = None, mes: Optional[str] = None):
        """
            Retorna a quantidade de vendas de um determinado consultor.
        """ 
        
        # Filtro para remover os valores estáticos
        dataframe = self.filter_by(ano, mes)
        dataframe = dataframe[dataframe['valor_acumulado'] > 0]
        return dataframe.shape[0]
    
    @property
    def meses_trabalhados(self):
        """
            Retorna a quantidade de meses que um consultor trabalhor. Valor é utilizado apenas como métrica
            para o cálculo de certas médias.
        """
        meses_trabalhados = self.dataframe['data'].nunique()

        return meses_trabalhados

    @property
    def years(self) -> list:
        """
            Retorna em formato de lista todos os anos em que 
            determinado consultor concluiu vendas.
        """

        years = list(self.dataframe['ano'].unique())

        return years
    
    def receita(self, ano: int = None, mes: str = None) -> float:

        """
            Retorna a receita total vendida pelo consultor

            Parâmetros
            ----------

            ano: int

                Parâmetro opcional, caso informado, irá retornar a
                receita total daquele ano
            
            mes: string

                Parâmetro opcional, caso informado, irá retornar a receita
                total daquele mês. Deve informar o ano caso utilize-o.
        """
        dataframe = self.filter_by(ano, mes)

        return float(dataframe['valor_acumulado'].sum())

    def quantidade(self, ano: Optional[int] = None, mes: Optional[str] = None) -> int:

        """
            Retorna a quantidade de produtos vendida pelo consultor

            Parâmetros
            ----------

            ano: int

                Parâmetro opcional, caso informado, irá retornar a
                quantidade total daquele ano
            
            mes: string

                Parâmetro opcional, caso informado, irá retornar a quantidade
                total daquele mês. Deve informar o ano caso utilize-o.
        """
            
        dataframe = self.filter_by(ano, mes)

        return int(dataframe['quantidade_de_produtos'].sum())
    
    @property
    def ticket_medio(self) -> int:

        """
            Retorna o ticket médio de vendas de determinado consultor

            Cálculo utilizado
            -------

            ``receita_total / quantidade_de_vendas ``
        """

        ticket_medio = self.receita() / self.quantidade_clientes()

        return ticket_medio
    
    @property
    def receita_media_mensal(self) -> int:

        """
            Retorna a média de vendas mensal de determinado consultor

            Cálculo utilizado
            -------

            ``receita_total / (anos * 12)``
        """

        receita_media_mensal = self.receita() / self.meses_trabalhados

        return receita_media_mensal
    
    @property
    def quantidade_media_mensal(self) -> int:

        """
            Retorna a média da quantidade de vendas mensal de determinado consultor

            Cálculo utilizado
            -------

            ``quantidade_total / (anos * 12)
        """

        quantidade_media_mensal = self.quantidade() / self.meses_trabalhados

        return quantidade_media_mensal
    
    def delta_receita_mensal(self, ano: int, mes: str) -> int:
        """
            Retorna o valor do parâmetro ``delta`` para a função ``col.metric`` do streamlit

            O ``delta_receita_mensal`` é a diferença entre a receita do mês referência 
            comparado com a receita do mês passado.

            Parâmetros
            ---------

            ano : int
            
                O ano atual que servirá como referência para o ``delta``

            mes : str

                O mês atual que servirá como referência para o ``delta`` 
        """

        delta_receita_mensal = self.__calculate_delta_metric__(self.receita, ano, mes)

        return delta_receita_mensal
    
    def delta_quantidade_mensal(self, ano: int, mes: str) -> int:
        """
            Retorna o valor do parâmetro ``delta`` para a função ``col.metric`` do streamlit

            O ``delta_receita_mensal`` é a diferença entre a quantidade de vendas do mês referência 
            comparado com a quantidade de vendas do mês passado.

            Parâmetros
            ---------

            ano : int
            
                O ano atual que servirá como referência para o ``delta``

            mes : str

                O mês atual que servirá como referência para o ``delta`` 
        """
        delta_quantidade_mensal = self.__calculate_delta_metric__(self.quantidade, ano, mes)

        return delta_quantidade_mensal
    
    def delta_quantidade_clientes(self, ano: int, mes: str) -> int:
        """
            Retorna o valor do parâmetro ``delta`` para a função ``col.metric`` do streamlit

            O ``delta_receita_mensal`` é a diferença entre a quantidade de vendas do mês referência 
            comparado com a quantidade de vendas do mês passado.

            Parâmetros
            ---------

            ano : int
            
                O ano atual que servirá como referência para o ``delta``

            mes : str

                O mês atual que servirá como referência para o ``delta`` 
        """
        delta_quantidade_clientes = self.__calculate_delta_metric__(self.quantidade_clientes, ano, mes)

        return delta_quantidade_clientes
    
    def receita_media_diaria(self, ano: int = None, mes: str = None) -> float:

        """
            Retorna a média da receita total diária de um determinado consultor 

            Parâmetros
            ---------

            ano : int | None

                O ano que você deseja ver a média. 
            
            mes : int | None

                O mês que você deseja ver a média.

            Cálculo Utilizado
            ---------

            ``receita_total`` / ``dias_trabalhados``
        """

        receita_media_diaria = self.receita(ano, mes) / self.dias_trabalhados

        return receita_media_diaria
    
    def quantidade_media_diaria(self, ano: int = None, mes: str = None) -> int:

        """
            Retorna a média da quantidade de produtos vendidos diariamente de um determinado consultor 

            Parâmetros
            ---------

            ano : int | None

                O ano que você deseja ver a média. 
            
            mes : int | None

                O mês que você deseja ver a média.

            Cálculo Utilizado
            ---------

            ``quantidade_total`` / ``dias_trabalhados``
        """

        quantidade_media_diaria = self.quantidade(ano, mes) / self.dias_trabalhados

        return quantidade_media_diaria
    
    def groupby_mes(self, ano: int) -> pd.DataFrame:

        """
            Agrupa o total de vendas de cada mês realizadas por um determinado consultor

            Parâmetros
            ------

            ano : int

                O ano que você deseja analisar 
        """
        meses_numeros = {
            'Janeiro': 1,
            'Fevereiro': 2,
            'Março': 3,
            'Abril': 4,
            'Maio': 5,
            'Junho': 6,
            'Julho': 7,
            'Agosto': 8,
            'Setembro': 9,
            'Outubro': 10,
            'Novembro': 11,
            'Dezembro': 12
        }

        dataframe = self.dataframe[
            (self.dataframe['ano'] == ano)
        ]

        dataframe_grouped = dataframe.groupby('mês').sum(numeric_only = True)

        # Transforma o index do dataframe em coluna, dessa forma é possível colocar a coluna MÊS em ordem.
        vendas_mensais_T = dataframe_grouped.T
        columns = list(vendas_mensais_T.columns)
        
        meses = sorted(columns, key=lambda x: meses_numeros[x])

        vendas_mensais = vendas_mensais_T[meses].T.reset_index()

        return vendas_mensais
    
    def groupby_ano(self) -> pd.DataFrame:

        """
            Retorna um dataframe com a receita de cada ano deum determinado consultor
        """

        dataframe_grouped = self.dataframe.groupby('ano', as_index = False).sum(numeric_only = True)
        vendas_anuais = dataframe_grouped.sort_values(by = 'ano', ascending = True)

        return vendas_anuais
    
    def groupby_produto(self) -> pd.DataFrame:

        """
            Retorna um dataframe com a receita total vendida por cada produto
        """

        dataframe_grouped = self.dataframe.groupby('tipo', as_index = False).sum(numeric_only = True)
        receita_por_produto = dataframe_grouped.sort_values(by = 'valor_acumulado', ascending = False)

        return receita_por_produto
    
    def __calculate_delta_metric__(self, metric_function, ano: int = None, mes: str = None) -> int:
            """
                Retorna o ``delta`` da métrica calculada por consultor de um determinado período.
                O valor é utilizado como parâmetro para a função ``st.metrics`` do streamlit.
            """
            
            # Caso o ano e mês anterior ao informado seja o primeiro mês com ocorrências de venda. O valor retornado é 0 
            
            ano = int(ano)
            
            if ano == min(self.years) and mes == None:
                return 0
            
            if ano == min(self.years) and mes.lower() == 'janeiro':
                return 0
            
            if mes:
                mes = mes.capitalize()

                ano_delta = ano - 1 if mes == 'Janeiro' else ano
                index_mes_passado = meses.index(mes) - 1
                mes_delta = meses[index_mes_passado]

                return metric_function(ano, mes) - metric_function(ano_delta, mes_delta)
            else:
                ano_delta = ano - 1 if ano != min(self.years) else ano
                return metric_function(ano) - metric_function(ano_delta)