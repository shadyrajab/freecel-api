import pandas as pd 
from database.objects import meses, dataframe_geral

from structures.consultores.metrics.delta import DeltaMetrics
from dataframe.dataframe import DataFrame

class PrivateMethods(
    DeltaMetrics
    ):

    def __init__(self, name):
        self.name = name

        self.dataframe = dataframe_geral[
            (dataframe_geral['CONSULTOR'] == name)
        ]

        super().__init__(dataframe = self.dataframe)
    
    def __formatar_nomes__(self) -> None:
        # Função para formatar o nome dos consultores 
        def formatar_nome(nome):
            try:
                nome_splited = nome.split(' ')
                if nome_splited[1] == 'DE' or nome_splited[1] == 'DOS':
                    nome = nome_splited[0] + ' ' + nome_splited[1] + ' ' + nome_splited[2]
                else:
                    nome = nome_splited[0] + ' ' + nome_splited[1]
            except:
                pass

            return nome
        
        self.dataframe['CONSULTOR'] = self.dataframe['CONSULTOR'].apply(lambda nome: formatar_nome(nome))

    def __add_static_values__(self) -> None:
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
                'CNAE': [None],
                'FATURAMENTO': [None],
                'COLABORADORES': [None]
            })

            # Concatena o dataframe original com o dataframe estático.
            self.dataframe = pd.concat([static, self.__dataframe__])

    def __get_receita_ou_quantidade__(self, retorno, ano: int = None, mes: str = None) -> int:

        """
            Função privada para retornar a soma de certas colunas do dataframe.
            Irá somar todos os valores da coluna ``<retorno>``

            Parâmetros
            ---------

            retorno: str

                A coluna que deseja somar os valores. Deve ser ``VALOR ACUMULADO``ou 
                ``QUANTIDADE DE PRODUTOS`` 

            ano: int | None

                Filtra o dataframe por ano

            mes: str | None

                Filtra o dataframe por mês

        """

        dataframe = self.dataframe

        if ano:
            dataframe = dataframe[
                (dataframe['ANO'] == ano)
            ]
        
        if ano and mes:
            dataframe = dataframe[
                (dataframe['ANO'] == ano) &
                (dataframe['MÊS'] == mes)
            ]
            
        receita_total = dataframe[retorno].sum()

        return receita_total
    
    def __get_media_mensal_receita_ou_quantidade__(self, retorno) -> int:

        """
            Função privada para retornar a média mensal da receita ou quantidade vendida 
            por determinado consultor

            Parâmetros 
            ----------

            retorno: str

                O nome da coluna que deseja retornar a média, deve ser 
                ``RECEITA`` ou ``QUANTIDADE``

        """

        quantidade_ou_receita = ''

        if retorno == 'RECEITA':
            quantidade_ou_receita = self.receita()

        if retorno == 'QUANTIDADE':
            quantidade_ou_receita = self.quantidade()

        media_mensal = quantidade_ou_receita / len(meses)

        return int(media_mensal)
    
    def __get_media_receita_ou_quantidade_diaria__(self, key: str, ano: int = None, mes: str = None) -> int:

        """
            Função privada que retorna a média da receita ou quantidade de produtos vendidos 
            diariamente de um determinado consultor 

            Parâmetros
            ---------

            key : str

                Se você deseja calcular a Receita ou Quantidade. Parâmetro deve ser ``RECEITA`` ou
                ``QUANTIDADE``

            ano : int | None

                O ano que você deseja ver a média. 
            
            mes : int | None

                O mês que você deseja ver a média.

            Cálculo Utilizado
            ---------

            ``receita_ou_quantidade_total`` / ``dias_trabalhados``
        """

        if ano and mes:
            dataframe = self.__dataframe__[
                (self.__dataframe__['ANO'] == ano) & 
                (self.__dataframe__['MÊS'] == mes)
            ]

        if key == 'RECEITA':
            key = 'VALOR ACUMULADO'
        
        elif key == 'QUANTIDADE':
            key = 'QUANTIDADE DE PRODUTOS'
        
        else:
            raise ValueError('O valor do parâmetro key deve ser RECEITA OU QUANTIDADE')

        receita_ou_quantidade_total = dataframe[key].sum()
        dias_trabalhados = self.dias_trabalhados

        media_diaria = receita_ou_quantidade_total / dias_trabalhados

        return media_diaria