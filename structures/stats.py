import pandas as pd
from database.dataframe import DataFrame
from typing import Optional
from utils.functions import calculate_delta

class Stats():
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def filter_by(self, ano: Optional[int] = None, mes: Optional[str] = None, tipo: Optional[str] = None) -> pd.DataFrame:
        return DataFrame.__filter_by__(
            dataframe = self.dataframe, 
            ano = ano, 
            mes = mes, 
            tipo = tipo
        )
    
    @property
    def dates(self) -> list[dict]:
        return [{f"{year}": self.months(year)} for year in self.years]
    
    @property
    def years(self) -> list[int]:
        return list(self.dataframe['ano'].unique())
    
    def months(self, ano) -> list[str]:
        return list(self.filter_by(ano)['mês'].unique())
    
    def periodo_trabalhado(self, ano: Optional[int] = None, mes: Optional[str] = None) -> int:
        if mes is not None: 
            return 22
        
        dataframe: pd.DataFrame = self.filter_by(ano)
        meses_trabalhados: int = dataframe['mês'].nunique()
        return meses_trabalhados
    
    def clientes(self, ano: Optional[int] = None, mes: Optional[str] = None) -> int:
        dataframe: pd.DataFrame = self.filter_by(ano, mes)
        return dataframe.shape[0]
    
    def receita(self, ano: Optional[int] = None, mes: Optional[str] = None) -> float:
        dataframe: pd.DataFrame = self.filter_by(ano, mes)
        return float(dataframe['valor_acumulado'].sum())

    def volume(self, ano: Optional[int] = None, mes: Optional[str] = None) -> int:
        dataframe: pd.DataFrame = self.filter_by(ano, mes)
        return int(dataframe['quantidade_de_produtos'].sum())
    
    def ticket_medio(self, ano: Optional[int] = None, mes: Optional[str] = None) -> int:
        return self.receita(ano, mes) / self.volume(ano, mes)
    
    def clientes_media(self, ano: Optional[int], mes: Optional[str] = None) -> int:
        return self.clientes(ano, mes) / self.periodo_trabalhado(ano, mes)
    
    def receita_media(self, ano: Optional[int], mes: Optional[str]) -> int:
        return self.receita(ano, mes) / self.periodo_trabalhado(ano, mes)
    
    def volume_media(self, ano: Optional[int], mes: Optional[str]) -> int:
        return self.volume(ano, mes) / self.periodo_trabalhado(ano, mes)
    
    def delta_clientes(self, ano: Optional[int] = None, mes: str = None) -> int:
        return calculate_delta(self.years, self.clientes, ano, mes)
    
    def delta_receita(self, ano: Optional[int] = None, mes: Optional[str] = None) -> int:
        return calculate_delta(self.years, self.receita, ano, mes)

    def delta_volume(self, ano: Optional[int] = None, mes: Optional[str] = None) -> int:
        return calculate_delta(self.years, self.volume, ano, mes)
    
    def delta_ticket_medio(self, ano: Optional[int] = None, mes: Optional[str] = None) -> int:
        return calculate_delta(self.years, self.ticket_medio, ano, mes)
    
    def delta_clientes_media(self, ano: Optional[int] = None, mes: Optional[str] = None) -> int:
        return calculate_delta(self.years, self.clientes, ano, mes)
    
    def delta_receita_media(self, ano: Optional[int] = None, mes: Optional[str] = None) -> int:
        return calculate_delta(self.years, self.receita_media, ano, mes)

    def delta_volume_media(self, ano: Optional[int] = None, mes: Optional[str] = None) -> int:
        return calculate_delta(self.years, self.volume, ano, mes)
    