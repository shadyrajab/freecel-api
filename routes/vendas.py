from fastapi import APIRouter, Depends, Query
from client.client import Client
from fastapi.encoders import jsonable_encoder
from authenticator.jwt import authenticate
from models.identify import ID
from models.vendas import Venda

router = APIRouter()

@router.get("/vendas", dependencies = [Depends(authenticate)])
def vendas(ano: int = Query(None, description = "Ano"), mes: str = Query(None, description = "Mês")):
    vendas = Client().vendas(ano, mes, True)
    return vendas

@router.put("/vendas", dependencies = [Depends(authenticate)])
def add_venda(venda: Venda):
    Client().add_venda(venda)
    return { "message": 'Venda adicionada com sucesso' }

@router.delete("/vendas", dependencies = [Depends(authenticate)])
def remove_venda(id: ID):
    Client().remove_venda(id)
    return { "message": 'Venda removida com sucesso' }