from structures.consultor import Consultor
from structures.ranking import Rankings
from database.dataframe import DataFrame
import pandas as pd

from typing import Optional

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
class Freecel(
    DataFrame
):
    def __init__(self, host, database, user, password):
        super().__init__(
            host,
            database,
            user,
            password
        )

    def filter_by(self, ano, mes):
        return DataFrame.__filter_by__(dataframe = self.dataframe, ano = ano ,mes = mes)

    def Consultor(self, nome, filtro: Optional[list] = None) -> Consultor:
        """
            Cria uma instância da classe ``Consultor``
        """

        return Consultor(nome, self.dataframe, filtro)
    
    def Ranking(self) -> Rankings:
        """
            Cria uma instância da classe ``Ranking``
        """

        return Rankings(self.dataframe)
    
    def years(self) -> list[int]:
        """
            Retorna uma lista com todos os anos com ocorrência de vendas
        """

        return list(self.dataframe['ano'].unique())

    def months(self, ano) -> list[str]:
        """
            Retorna uma lista com todos os meses de um determinado ano com ocorrência de vendas
        """

        return list(self.filter_by(ano)['mês'].unique())
    
    def consultores(self, ano: int = None, mes: str = None) -> list[str]:
        """
            Retorna uma lista com o nome de todos os consultores com ocorrências de vendas       
        """
        dataframe = self.filter_by(ano, mes)
        return list(dataframe['consultor'].unique())
    
    def ufs(self, ano: int = None, mes: str = None):
        """
            Retorna uma lista com todos as UF's com ocorrÊncias de vendas
        """

        dataframe = self.filter_by(ano, mes)
        return list(dataframe['uf'].unique())
    
    def maior_venda_mes(self) -> int:
        """
            Retorna o valor do mês que teve a maior receita
        """

        dataframe = self.dataframe.groupby('data', as_index = False).sum(numeric_only = True)

        return dataframe['valor_acumulado'].max()
    
    def delta_receita_total(self, ano: int = None, mes: str = None) -> int:
        """
            Retorna o ``delta`` da receita total de um determinado período.
            O valor é utilizado como parâmetro para a função ``st.metrics`` do streamlit.
        """

        return self.__calculate_delta_metric__(self.receita_total, ano, mes)

    def delta_quantidade_clientes(self, ano: int = None, mes: str = None) -> int:
        """
            Retorna o ``delta`` da receita total de um determinado período.
            O valor é utilizado como parâmetro para a função ``st.metrics`` do streamlit.
        """

        return self.__calculate_delta_metric__(self.quantidade_clientes, ano, mes)

    def delta_quantidade_produtos(self, ano: int = None, mes: str = None) -> int:
        """
            Retorna o ``delta`` da quantidade vendida de um determinado período.
            O valor é utilizado como parâmetro para a função ``st.metrics`` do streamlit.
        """

        return self.__calculate_delta_metric__(self.qtd_de_produtos_vendidos, ano, mes)

    def delta_quantidade_clientes(self, ano: int = None, mes: str = None) -> int:
        """
            Retorna o ``delta`` da quantidade vendida de um determinado período.
            O valor é utilizado como parâmetro para a função ``st.metrics`` do streamlit.
        """

        return self.__calculate_delta_metric__(self.quantidade_clientes, ano, mes)
    
    def delta_ticket_medio(self, ano: int = None, mes: str = None) -> int:
        """
            Retorna o ``delta`` do ticket médio de um determinado período.
            O valor é utilizado como parâmetro para a função ``st.metrics`` do streamlit.
        """

        return self.__calculate_delta_metric__(self.ticket_medio, ano, mes)

    def delta_media_diaria(self, ano: int = None, mes: str = None) -> int:
        """
            Retorna o ``delta`` da média diária de vendas de um determinado período.
            O valor é utilizado como parâmetro para a função ``st.metrics`` do streamlit.
        """
        return self.__calculate_delta_metric__(self.receita_media_diaria, ano, mes)

    def delta_media_por_consultor(self, ano: int = None, mes: str = None) -> int:
        """
            Retorna o ``delta`` da média por consultor de um determinado período.
            O valor é utilizado como parâmetro para a função ``st.metrics`` do streamlit.
        """
        return self.__calculate_delta_metric__(self.media_por_consultor, ano, mes)


    def qtd_vendas_por_cnae(self, ano: int = None, mes: str = None) -> pd.DataFrame:
        """
            Retorna um ``DataFrame`` com a quantidade de vendas por cada CNAE de empresa .

            codg: 'COD CNAE' | 'NOME CNAE'
                Se deseja agrupar pelo código do CNAE, ou pelo nome
        """         

        dataframe = self.filter_by(ano, mes)
        qtd_vendas_por_cnae = dataframe['nome_cnae'].value_counts().reset_index()

        return pd.DataFrame(qtd_vendas_por_cnae)
    
    def qtd_vendas_por_faturamento(self, ano: int = None, mes: str = None) -> pd.DataFrame:
        """
            Retorna um ``DataFrame`` com a quantidade de vendas por faturamento de empresa
        """

        dataframe = self.filter_by(ano, mes)
        qtd_vendas_por_faturamento = dataframe['faturamento'].value_counts().reset_index()

        return pd.DataFrame(qtd_vendas_por_faturamento)
    
    def qtd_vendas_por_colaboradores(self, ano: int = None, mes: str = None) -> pd.DataFrame:
        """
            Retorna um ``DataFrame`` com a quantidade de vendas por quantidade de colaboradores de empresa
        """

        dataframe = self.filter_by(ano, mes)
        qtd_vendas_colaboradores = dataframe['colaboradores'].value_counts().reset_index()

        return pd.DataFrame(qtd_vendas_colaboradores)

    def quantidade_clientes(self, ano: int = None, mes: str = None) -> int:

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

        return self.filter_by(ano, mes).shape[0]

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

        return self.filter_by(ano, mes)['valor_acumulado'].sum()
    
    def qtd_de_produtos_vendidos(self, ano: int = None, mes: str = None) -> int:

        """
            Retorna a receita total de vendas em um determinado período.

            #### Parâmetros 

            ano : int | None
                Parâmetro opcional, caso informado, retornará a receita do ano inteiro

            mes : str | None
                Parâmetro opcional, caso informado, retornará a receita daquele mês. O parâmetro 
                ``ano`` é obrigatório caso ``mes`` seja passado. 
        """

        return int(self.filter_by(ano, mes)['quantidade_de_produtos'].sum())
    
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

        return self.receita_total(ano, mes) / self.quantidade_clientes(ano, mes)

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

        dataframe: pd.DataFrame = self.filter_by(ano, mes)
        consultor_nome: str = dataframe.groupby('consultor')['valor_acumulado'].sum().idxmax()
        consultor_do_mes: Consultor = self.Consultor(consultor_nome, [ano, mes])

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
    
    def media_por_consultor(self, ano: int = None, mes: str = None) -> float:

        """
            Retorna a receita média vendida por cada consultor em um determinado período.

            #### Parâmetros 

            ano : int | None
                Parâmetro opcional, caso informado, retornará a media do ano inteiro

            mes : str | None
                Parâmetro opcional, caso informado, retornará a media daquele mês. O parâmetro 
                ``ano`` é obrigatório caso ``mes`` seja passado. 
        """

        dataframe: pd.DataFrame = self.filter_by(ano, mes)
        consultores: int = dataframe['consultor'].nunique() # -> Quantidade de consultores
        media_por_consultor: int = self.receita_total(ano, mes) / consultores

        return media_por_consultor

    def __calculate_delta_metric__(self, metric_function, ano: int = None, mes: str = None) -> int:
        """
            Retorna o ``delta`` da métrica calculada por consultor de um determinado período.
            O valor é utilizado como parâmetro para a função ``st.metrics`` do streamlit.
        """
        
        # Caso o ano e mês anterior ao informado seja o primeiro mês com ocorrências de venda. O valor retornado é 0 
        
        ano = int(ano)
        mes = mes.capitalize()

        if ano == min(self.years()) and mes == 'Janeiro':
            return 0

        ano_delta = ano - 1 if mes == 'Janeiro' else ano
        index_mes_passado = meses.index(mes) - 1
        mes_delta = meses[index_mes_passado]

        return metric_function(ano, mes) - metric_function(ano_delta, mes_delta)
    