from fastapi import FastAPI
from dotenv import load_dotenv
from os import getenv
from client.client import Freecel
from typing import Optional

load_dotenv()

HOST = getenv('host')
DATABASE = getenv('database')
USER = getenv('user')
PASSWORD = getenv('password')

client = Freecel(
    host = HOST,
    database = DATABASE,
    user = USER,
    password = PASSWORD
)

app = FastAPI()

def get_freecel_data(ano: Optional[int] = None, mes: Optional[str] = None):
    if ano is not None and mes is not None:
        mes = mes.capitalize()
    
    return {
        "receita": client.receita_total(ano, mes),
        "quantidade_produtos_vendidos": client.qtd_de_produtos_vendidos(ano, mes),
        "media_por_consultor": client.media_por_consultor(ano, mes),
        "quantidade_vendas": client.quantidade_de_vendas(ano, mes),
        "ticket_medio": client.ticket_medio(ano, mes)
    }

def get_consultor_data(nome_consultor: str, ano: Optional[int] = None, mes: Optional[str] = None):
    nome_consultor = nome_consultor.replace('_', ' ').upper()
    if mes is not None:
        mes = mes.capitalize()
    
    consultor = client.Consultor(nome_consultor)
    
    return {
        "name": consultor.name,
        "receita_total": consultor.receita(),
        "quantidade_vendida": consultor.quantidade(),
        "receita_media_diaria": consultor.media_receita_diaria(),
        "ticket_medio": consultor.ticket_medio,
        "quantidade_media_diaria": consultor.media_quantidade_diaria(),
        "quantidade_clientes": consultor.quantidade_clientes,
        "quantidade_media_mensal": consultor.quantidade_media_mensal,
        "receita_media_mensal": consultor.receita_media_mensal,
    }


@app.get("/")
def home():
    return {"message": "ghghggk"}

@app.get("/freecel")
def freecel():
    return get_freecel_data()

@app.get("/freecel/{ano}/{mes}")
def freecel(ano: int, mes: str):
    return get_freecel_data(ano, mes)

@app.get("/consultor/{nome_consultor}")
def consultor(nome_consultor: str):
    return get_consultor_data(nome_consultor)

@app.get("/consultor/{nome_consultor}/{ano}/{mes}")
def consultor(nome_consultor: str, ano: int, mes: str):
    return get_consultor_data(nome_consultor, ano, mes)

@app.get("/consultores")
def consultores():
    return {
        "consultores": client.consultores()
    }