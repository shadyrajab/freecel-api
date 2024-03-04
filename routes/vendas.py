from fastapi import APIRouter, Depends, Query
from client.instance import client
from fastapi.encoders import jsonable_encoder
from authenticator.jwt import authenticate
from models.identify import ID

router = APIRouter()

@router.get("/vendas", dependencies = [Depends(authenticate)])
def vendas(ano: int = Query(None, description = "Ano"), mes: str = Query(None, description = "Mês")):
    vendas = client.vendas(ano, mes, True)
    return jsonable_encoder(vendas)

# @router.put("/vendas", dependencies = [Depends(authenticate)])
# def add_venda(venda: Venda):
#     client.add_venda(venda)
#     return { "message": 'Venda adicionada com sucesso' }

@router.delete("/vendas", dependencies = [Depends(authenticate)])
def remove_venda(id: ID):
    client.remove_venda(id)
    return { "message": 'Venda removida com sucesso' }