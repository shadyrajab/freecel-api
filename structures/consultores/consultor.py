import pandas as pd
from structures.consultores.private_methods import PrivateMethods
from dataframe.dataframe import DataFrame

class Consultor(
    PrivateMethods,
    ):
    def __init__(self, name):
        super().__init__(name = name)

    @property
    def dias_trabalhados(self) -> int:
        """
            Retorna quantos dias determinado consultor trabalhou aproximadamente. Valor é utilizado como
            métrica para o cálculo de certas médias

        """

        dataframe = self.dataframe

        # Concatena as colunas ``MÊS`` e ``ANO`` em uma única
        dataframe['DATA'] = dataframe['MÊS'] + '/' + dataframe['ANO']

        meses_trabalhados = list(dataframe['DATA'].unique())

        # Soma a quantidade de meses tabalhados com a quantidade de dias úteis de um mês
        dias_trabalhados = len(meses_trabalhados) * 22

        return dias_trabalhados

    @property
    def years(self) -> list:
        """
            Retorna em formato de lista todos os anos em que 
            determinado consultor concluiu vendas.
        """
        years = list(self.dataframe['ANO'].unique())

        return years
    
    def receita(self, ano: int = None, mes: str = None) -> int:

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
            
        receita_total = self.__get_receita_ou_quantidade__(
            'VALOR ACUMULADO', ano, mes
        )

        return receita_total

    def quantidade(self, ano: int = None, mes: str = None) -> int:

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
            
        quantidade_total = self.__get_receita_ou_quantidade__(
            'QUANTIDADE DE PRODUTOS', ano, mes
        )

        return quantidade_total
    
    @property
    def ticket_medio(self) -> int:

        """
            Retorna o ticket médio de vendas de determinado consultor

            Cálculo utilizado
            -------

            ``receita_total / quantidade_de_vendas ``
        """

        receita_total = self.receita()
        quantidade_de_vendas = self.dataframe.shape[0]

        ticket_medio = receita_total / quantidade_de_vendas

        return ticket_medio
    
    @property
    def receita_media_mensal(self) -> int:

        """
            Retorna a média de vendas mensal de determinado consultor

            Cálculo utilizado
            -------

            ``receita_total / (anos * 12)
        """

        receita_media_mensal = self.__get_media_mensal_receita_ou_quantidade__('RECEITA')

        return receita_media_mensal
    
    @property
    def quantidade_media_mensal(self) -> int:

        """
            Retorna a média da quantidade de vendas mensal de determinado consultor

            Cálculo utilizado
            -------

            ``quantidade_total / (anos * 12)
        """

        quantidade_media_mensal = self.__get_media_mensal_receita_ou_quantidade__('QUANTIDADE')

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

        delta_receita_mensal = self.__get_delta_receita_ou_quantidade_mensal__(ano, mes, 'RECEITA')

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

        delta_quantidade_mensal = self.__get_delta_receita_ou_quantidade_mensal__(ano, mes, 'QUANTIDADE')

        return delta_quantidade_mensal
    
    def media_receita_diaria(self, ano: int = None, mes: str = None) -> int:

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

        receita_media_diaria = self.__get_media_receita_ou_quantidade_diaria__(
            self, 'RECEITA', ano, mes
        )

        return receita_media_diaria
    
    def media_quantidade_diaria(self, ano: int = None, mes: str = None) -> int:

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

        quantidade_media_diaria = self.__get_media_receita_ou_quantidade_diaria__(
            self, 'QUANTIDADE', ano, mes
        )

        return quantidade_media_diaria
    
    def groupby_mes(self, ano: int) -> pd.DataFrame:

        """
            Agrupa o total de vendas de cada mês realizadas por um determinado consultor

            Parâmetros
            ------

            ano : int

                O ano que você deseja analizar 
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
            (self.dataframe['ANO'] == ano)
        ]

        dataframe_grouped = dataframe.groupby('MÊS').sum(numeric_only = True)

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

        dataframe_grouped = self.dataframe.groupby('ANO', as_index = False).sum(numeric_only = True)
        vendas_anuais = dataframe_grouped.sort_values(by = 'ANO', ascending = True)

        return vendas_anuais
    
    def groupby_produto(self) -> pd.DataFrame:

        """
            Retorna um dataframe com a receita total vendida por cada produto
        """

        dataframe_grouped = self.dataframe.groupby('TIPO', as_index = False).sum(numeric_only = True)
        receita_por_produto = dataframe_grouped.sort_values(by = 'VALOR ACUMULADO', ascending = False)

        return receita_por_produto