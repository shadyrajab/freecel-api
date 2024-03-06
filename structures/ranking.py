import pandas as pd
from typing import Optional
from database.dataframe import DataFrame
from utils.variables import TIPO_VENDA
from utils.functions import jsonfy

class Rankings:
    def __init__(self, dataframe: pd.DataFrame, ano: Optional[int] = None, mes: Optional[str] = None, jsonfy: Optional[bool] = None):
        self.dataframe = self.filter_by(dataframe, ano, mes)
        self.jsonfy = jsonfy
        self.ano = ano
        self.mes = mes.capitalize() if mes else mes

    def filter_by(self, dataframe: pd.DataFrame, ano: Optional[int] = None, mes: Optional[str] = None, tipo: Optional[str] = None) -> pd.DataFrame:
        return DataFrame.__filter_by__(
            dataframe = dataframe, 
            ano = ano, 
            mes = mes, 
            tipo = tipo
        )
    
    @property
    def consultores_geral(self):
        return self.__ranking_consultores()
    
    @property
    def consultores_altas(self):
        return self.__ranking_consultores('ALTAS')
    
    @property
    def consultores_fixa(self):
        return self.__ranking_consultores('FIXA')
    
    @property
    def consultores_avancada(self):
        return self.__ranking_consultores('AVANÇADA')
    
    @property
    def consultores_migracao(self):
        return self.__ranking_consultores('MIGRAÇÃO PRÉ-PÓS')
    
    @property
    def consultores_vvn(self):
        return self.__ranking_consultores('VVN')
    
    @property
    def consultores_portabilidade(self):
        return self.__ranking_consultores('PORTABILIDADE')

    @property
    def planos(self):
        return self.__get_ranking('plano')
    
    @property
    def produtos(self):
        return self.__get_ranking('tipo')

    @property
    def geral(self) -> pd.DataFrame:
        return self.__get_ranking('consultor')

    @property
    def fixa(self) -> pd.DataFrame:
        return self.__get_ranking('consultor', 'FIXA')
    
    @property
    def avancada(self) -> pd.DataFrame:
        return self.__get_ranking('consultor', 'AVANÇADA')
    
    @property
    def vvn(self) -> pd.DataFrame:
        return self.__get_ranking('consultor', 'VVN')
    
    @property
    def migracao(self) -> pd.DataFrame:
        return self.__get_ranking('consultor', 'MIGRAÇÃO PRÉ-PÓS')
    
    @property
    def altas(self) -> pd.DataFrame:
        return self.__get_ranking('consultor', 'ALTAS')

    @property
    def portabilidade(self) -> pd.DataFrame:
        return self.__get_ranking('consultor', 'PORTABILIDADE')
    
    @property
    def periodo_trabalhado(self) -> int:
        dataframe = self.dataframe.copy()
        dataframe['periodo'] = dataframe['data'].dt.strftime('%m/%Y')
        meses_trabalhados = dataframe['periodo'].nunique()
        if meses_trabalhados <=1:
            return 22
        
        return meses_trabalhados
    
    def to_json(self):
        data = {}
        for cls in reversed(self.__class__.__mro__):
            for attr_name, attr_value in vars(cls).items():
                if isinstance(attr_value, property):
                    data[attr_name] = getattr(self, attr_name)

        return data
    
    def __ranking_consultores(self, tipo: Optional[str] = None):
        dataframe = self.filter_by(self.dataframe.copy(), tipo = tipo)
        dataframe = dataframe.groupby('consultor', as_index = False).sum(numeric_only=True)
        clientes = self.dataframe['consultor'].value_counts().reset_index()
        clientes.columns = ['consultor', 'clientes']

        final_dataframe = pd.merge(dataframe, clientes, on = 'consultor')
        final_dataframe['ticket_medio'] = final_dataframe['valor_acumulado'] / final_dataframe['clientes']
        final_dataframe['receita_media'] = final_dataframe['valor_acumulado'] / self.periodo_trabalhado
        final_dataframe['volume_media'] = final_dataframe['quantidade_de_produtos'] / self.periodo_trabalhado
        final_dataframe['clientes_media'] = final_dataframe['clientes'] / self.periodo_trabalhado
        final_dataframe.rename(columns = {'quantidade_de_produtos': 'volume', 'valor_acumulado': 'receita'}, inplace=True)
        final_dataframe.drop(columns=['ano', 'id', 'valor_do_plano'], inplace = True)
        if self.jsonfy:
            return jsonfy(final_dataframe)
        
        final_dataframe.to_excel('doidao.xlsx')
        
        return final_dataframe
    
    def __get_ranking(self, column: str, tipo_venda: Optional[str] = None) -> DataFrame:
        dataframe = self.dataframe.copy()
        if tipo_venda and tipo_venda not in TIPO_VENDA:
            raise ValueError(f"O tipo de venda deve ser {str(TIPO_VENDA)}")
        
        if tipo_venda:
            dataframe = self.filter_by(self.dataframe, tipo=tipo_venda)
            
        quantidade_de_vendas = dataframe[column].value_counts().reset_index()
        quantidade_de_vendas.columns = [column, 'quantidade_de_vendas']

        ranking = dataframe.groupby(column, as_index = False).sum(numeric_only = True)
        ranking.drop(['ano', 'valor_do_plano', 'id'], axis = 1, inplace = True)

        final_dataframe = pd.merge(ranking, quantidade_de_vendas, on = column)
        if self.jsonfy:
            return jsonfy(final_dataframe)
        
        return final_dataframe

