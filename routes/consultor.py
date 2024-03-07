from fastapi import APIRouter, Depends, Query
from client.client import Client
from fastapi.encoders import jsonable_encoder
from models.consultor import Vendedor
from authenticator.jwt import authenticate
from models.identify import ID

router = APIRouter()

@router.get("/consultores", dependencies = [Depends(authenticate)])
def consultores():
    consultores = Client().consultores(True)
    return jsonable_encoder(consultores)

@router.put("/consultores", dependencies = [Depends(authenticate)])
def add_consultor(consultor: Vendedor):
    Client().add_consultor(consultor)
    return {'message': 'Consultor adicionado com sucesso'}

@router.delete("/consultores", dependencies = [Depends(authenticate)])
def remove_consultor(id: ID):
    Client().remove_consultor(id)
    return {"message": 'Consultor removido com sucesso'}

@router.get("/consultores/{nome_consultor}", dependencies = [Depends(authenticate)])
def consultor(nome_consultor: str, ano: int = Query(None, description = "Ano"), mes: str = Query(None, description = "Mês"), display_vendas: bool = Query(None, description = "Mostrar vendas")):
    nome_consultor = nome_consultor.replace('_', ' ').upper()
    consultor = Client().Consultor(nome_consultor, ano, mes, True, display_vendas)
    return jsonable_encoder(consultor.to_json())