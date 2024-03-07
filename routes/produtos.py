from fastapi import APIRouter, Depends
from client.client import Client
from fastapi.encoders import jsonable_encoder
from authenticator.jwt import authenticate
from models.identify import ID
from models.produtos import Produto

router = APIRouter()

@router.get("/produtos", dependencies = [Depends(authenticate)])
def produtos():
    produtos = Client().produtos(True)
    return jsonable_encoder(produtos)

@router.put("/produtos", dependencies = [Depends(authenticate)])
def add_produto(produto: Produto):
    Client().add_produto(produto)
    return {"message": "Produto adicionado com sucesso"}

@router.delete("/produtos", dependencies = [Depends(authenticate)])
def remove_produto(id: ID):
    Client().remove_produto(id)
    return {"message": 'Produto removido com sucesso'}