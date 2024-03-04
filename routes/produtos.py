from fastapi import APIRouter, Depends
from client.instance import client
from fastapi.encoders import jsonable_encoder
from authenticator.jwt import authenticate
from models.identify import ID
from models.produtos import Produto

router = APIRouter()

@router.get("/produtos", dependencies = [Depends(authenticate)])
def produtos():
    produtos = client.produtos(True)
    return jsonable_encoder(produtos)

@router.put("/produtos", dependencies = [Depends(authenticate)])
def add_produto(produto: Produto):
    client.add_produto(produto)
    return {"message": "Produto adicionado com sucesso"}

@router.delete("/produtos", dependencies = [Depends(authenticate)])
def remove_produto(id: ID):
    client.remove_produto(id)
    return {"message": 'Produto removido com sucesso'}