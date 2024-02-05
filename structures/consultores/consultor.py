import pandas as pd
from dataframe.dataframe import DataFrame

from typing import Optional

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

class Consultor():
    def __init__(self, name, dataframe, filtro: Optional[list] = None):
        self.name = name
        self.dataframe = dataframe[
            (dataframe['CONSULTOR'] == name)
        ]

        if filtro:
            ano, mes = filtro
            self.dataframe = DataFrame.filter_by(self.dataframe, ano, mes)

        self.__add_static_values__()

    def filter_by(self, ano, mes):
        return DataFrame.filter_by(self.dataframe, ano , mes)

    @property
    def dias_trabalhados(self) -> int:
        """
            Retorna quantos dias determinado consultor trabalhou aproximadamente. Valor é utilizado como
            métrica para o cálculo de certas médias

        """

        # Soma a quantidade de meses tabalhados com a quantidade de dias úteis de um mês
        dias_trabalhados = len(self.meses_trabalhados) * 22
        
        return dias_trabalhados
    
    @property
    def quantidade_clientes(self):
        """
            Retorna a quantidade de vendas de um determinado consultor.
        """ 
        
        # Filtro para remover os valores estáticos
        dataframe = self.dataframe[self.dataframe['VALOR ACUMULADO'] > 0]
        return dataframe.shape[0]
    
    @property
    def meses_trabalhados(self):
        """
            Retorna a quantidade de meses que um consultor trabalhor. Valor é utilizado apenas como métrica
            para o cálculo de certas médias.
        """
        meses_trabalhados = self.dataframe['DATA'].nunique()

        return meses_trabalhados

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
            
        dataframe = self.filter_by(ano, mes)

        return dataframe['VALOR ACUMULADO'].sum()

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
            
        dataframe = self.filter_by(ano, mes)

        return dataframe['QUANTIDADE DE PRODUTOS'].sum()
    
    @property
    def ticket_medio(self) -> int:

        """
            Retorna o ticket médio de vendas de determinado consultor

            Cálculo utilizado
            -------

            ``receita_total / quantidade_de_vendas ``
        """

        ticket_medio = self.receita() / self.quantidade_clientes

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
    
    def __get_delta_receita_ou_quantidade_mensal__(self, ano: int, mes: str, key: str) -> int:
        """
        Calcula o delta entre a receita ou quantidade de vendas do mês de referência e o mês anterior.

        Parâmetros
        ----------
        ano : int
            O ano atual que servirá como referência para o cálculo do delta.
        mes : str
            O mês atual que servirá como referência para o cálculo do delta.
        key : str
            O nome da coluna para o qual deseja-se calcular o delta. Deve ser "RECEITA" ou "QUANTIDADE".

        Retorna
        -------
        int
            O valor do delta entre a média do mês atual e do mês passado.
        """
        if key not in {'RECEITA', 'QUANTIDADE'}:
            raise ValueError('O valor do parâmetro key deve ser "RECEITA" ou "QUANTIDADE".')

        primeiro_ano = min(self.years)

        # Retorna 0 caso não haja venda anterior ao mês e ano referência.
        if ano == primeiro_ano and mes == 'Janeiro':
            return 0 

        # Se o mês referência for Janeiro, então o ano referência será o ano passado.
        ano_delta = ano - 1 if mes == 'Janeiro' else ano

        index_mes_passado = meses.index(mes) - 1
        mes_delta = meses[index_mes_passado]

        media_atual = self.receita(ano=ano, mes=mes) if key == 'RECEITA' else self.quantidade(ano=ano, mes=mes)
        media_mes_passado = self.receita(ano_delta, mes_delta) if key == 'RECEITA' else self.quantidade(ano_delta, mes_delta)

        return media_atual - media_mes_passado

    def __add_static_values__(self):
        """
            Adiciona vendas estáticas ao dataframe de determinado consultor.
            A função foi criada para ajudar na plotagem dos gráficos, fazendo com 
            que fique visível os meses cujo consultor não tenha vendido produtos.
        """

        # Retorna o último ano que o consultor realizou uma venda.
        ultimo_ano = max(self.years)

        for mes in meses:
            static = pd.DataFrame({
                'UF': [None],
                'CNPJ': [None],
                'MÊS': [mes],
                'ANO': [ultimo_ano],
                'PLANO': [None],
                'TIPO': [None],
                'VALOR DO PLANO': [0],
                'QUANTIDADE DE PRODUTOS': [0],
                'VALOR ACUMULADO': [0],
                'CONSULTOR': [None],
                'GESTOR': [None],
                'REVENDA': [None],
                'FATURAMENTO': [None],
                'COLABORADORES': [None],
                'COD CNAE': [None],
                'NOME CNAE': [None],
            })

            # Concatena o dataframe original com o dataframe estático.
            self.dataframe = pd.concat([static, self.dataframe])