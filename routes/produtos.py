from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from models.identify import ID
from models.produtos import Produto
from params.request_body import UpdateProdutoParams

router = APIRouter()


@router.get("/produtos", dependencies=[Depends(authenticate)])
async def produtos():
    async with Client() as client:
        produtos = await client.produtos(True)
        return produtos


@router.post("/produtos", dependencies=[Depends(authenticate)])
async def add_produto(produto: Produto):
    async with Client() as client:
        await client.add_produto(produto)
        return {"message": "Produto adicionado com sucesso"}


@router.put("/produtos", dependencies=[Depends(authenticate)])
async def update_produto(params: UpdateProdutoParams):
    async with Client() as client:
        await client.update_produto(**params.model_dump())
        return {"message": "Produto atualizado com sucesso"}


@router.delete("/produtos", dependencies=[Depends(authenticate)])
async def remove_produto(id: ID):
    async with Client() as client:
        await client.remove_produto(id)
        return {"message": "Produto removido com sucesso"}
