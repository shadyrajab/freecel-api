from fastapi import FastAPI, Query
from fastapi.encoders import jsonable_encoder
from client.client import Freecel

from responses import Consultor, Freecel, Crm

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ghghggk"}

@app.get("/freecel")
def freecel(
        display_vendas: bool = Query(None, description = 'Mostrar vendas (opcional)'), 
        ano: int = Query(None, description = "Ano (opcional)"), 
        mes: str = Query(None, description = "Mês (opcional)")
    ):

    freecel = Freecel(display_vendas, ano, mes)

    return jsonable_encoder(freecel)

@app.get("/consultor/{nome_consultor}")
def consultor(
        nome_consultor: str,
        display_vendas: bool = Query(None, description = 'Mostrar vendas (opcional)'), 
        ano: int = Query(None, description = "Ano (opcional)"), 
        mes: str = Query(None, description = "Mês (opcional)")
    ):

    nome_consultor = nome_consultor.replace('_', ' ').upper()
    consultor = Consultor(nome_consultor, display_vendas, ano, mes)

    return jsonable_encoder(consultor)

@app.get('/crm')
def crm():
    return Crm
    