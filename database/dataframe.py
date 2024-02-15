import pandas as pd
from database.connection import DataBase

from typing import Optional

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

class DataFrame(
    DataBase
):
    def __init__(self, host, database, user, password):
        super().__init__(
            host = host, 
            database = database, 
            user = user, 
            password = password
        )
        
        self.dataframe = self.__get_full_dataframe__()
        self.crm = self.__get_crm_dataframe__()
        self.__dataframe_replace__()
        self.__formatar_nomes__()
        self.__formatar_datas__()
        self.__formatar_tipo_colunas__()
        
        self.cursor.close()
        self.connection.close()

    def __formatar_tipo_colunas__(self) -> None:
        self.dataframe[['valor_acumulado', 'valor_do_plano', 'quantidade_de_produtos']] = self.dataframe[
                ['valor_acumulado', 'valor_do_plano', 'quantidade_de_produtos']
            ].apply(pd.to_numeric, errors='coerce', downcast='integer')

    def __formatar_datas__(self) -> None:
        def get_mes(mes):
            return meses[mes - 1]

        self.dataframe['ano'] = pd.to_datetime(self.dataframe['data']).dt.year
        self.dataframe['mês'] = pd.to_datetime(self.dataframe['data']).dt.month.apply(lambda mes: get_mes(mes))


    def __formatar_nomes__(self):
        def formatar_nome(nome):
            nome_splited = nome.split(' ')
            try:
                if nome_splited[1] == 'DE' or nome_splited[1] == 'DOS':
                    nome = nome_splited[0] + ' ' + nome_splited[1] + ' ' + nome_splited[2]
                else:
                    nome = nome_splited[0] + ' ' + nome_splited[1]
            except:
                pass

            return nome

        self.dataframe['consultor'] = self.dataframe['consultor'].apply(lambda n: formatar_nome(n))

    def __dataframe_replace__(self) -> None:
        self.dataframe.replace({
            'JÁ CLIENTE': 'ALTAS', 
            'NOVO': 'ALTAS', 
            'PORTABILIDADE': 'ALTAS',
            'PORTABILIDADE PF + TT PF/PJ - VIVO TOTAL': 'ALTAS',
            'INTERNET': 'ALTAS',
            'PORTABILIDADE - VIVO TOTAL': 'ALTAS',
            'PORTABILIDADE PF + TT PF/PJ': 'ALTAS',
            'NOVO - VIVO TOTAL': 'ALTAS',
            'PORTABILIDADE CNPJ – CNPJ': 'ALTAS',

            'MIGRAÇÃO PRÉ/PÓS': 'MIGRAÇÃO PRÉ-PÓS',
            'MIGRAÇÃO PRÉ/PÓS - VIVO TOTAL': 'MIGRAÇÃO PRÉ-PÓS',

            'MIGRAÇÃO': 'MIGRAÇÃO PRÉ-PÓS',
            'MIGRAÇÃO PRÉ/PÓS_TOTALIZACAO': 'MIGRAÇÃO PRÉ-PÓS',

            'INTERNET_TOTALIZACAO': 'ALTAS',
            'MIGRAÇÃO+TROCA': 'MIGRAÇÃO PRÉ-PÓS',
            'NOVO_TOTALIZACAO': 'ALTAS',

            'JÁ CLIENTE - VIVO TOTAL': 'ALTAS',
            'MIGRAÇÃO PRÉ/PÓS + TROCA': 'MIGRAÇÃO PRÉ-PÓS'

        }, inplace=True)

    def __get_full_dataframe__(self):
        self.cursor.execute('SELECT * FROM vendas_concluidas')
        data = self.cursor.fetchall()

        dataframe = pd.DataFrame(data, columns=[desc[0] for desc in self.cursor.description])
        
        return dataframe
    
    def __get_crm_dataframe__(self):
        self.cursor.execute('SELECT * from crm')
        data = self.cursor.fetchall()
        dataframe = pd.DataFrame(data, columns=[desc[0] for desc in self.cursor.description])
        
        return dataframe

    @staticmethod
    def __filter_by__(
        dataframe, ano: Optional[int] = None, mes: Optional[str] = None, consultor: Optional[str] = None,
        tipo: Optional[str] = None):

        """
        Filtra um DataFrame com base nos parâmetros fornecidos.

        Parâmetros
        ----------
        dataframe : pd.DataFrame
            O DataFrame a ser filtrado.

        ano : int | None
            O ano para o qual deseja filtrar os dados.

        mes : str | None
            O mês para o qual deseja filtrar os dados.

        consultor : str | None
            O nome do consultor para o qual deseja filtrar os dados.

        Retorna
        -------
        pd.DataFrame
            O DataFrame filtrado.
        """
        # Verifica o formato do mês

        if mes:
            mes = mes.capitalize()

        if ano:
            ano = int(ano)

        if tipo:
            tipo = tipo.upper()

        if consultor:
            consultor = consultor.upper()

        if mes and mes not in meses:
            raise ValueError('Formato de mês inválido. Por favor, escreva o nome do mês completo com acentos.')
    
        # Aplica os filtros
        filters = {
            'ano': ano,
            'mês': mes,
            'consultor': consultor,
            'tipo': tipo
        }

        for column, value in filters.items():
            if value is not None:
                dataframe = dataframe[dataframe[column] == value]

        return dataframe

