from fastapi import APIRouter, Depends, Query
from client.client import Client
from authenticator.jwt import authenticate
from models.identify import ID
from models.vendas import Venda

router = APIRouter()

@router.get("/vendas", dependencies = [Depends(authenticate)])
async def vendas(ano: int = Query(None, description = "Ano"), mes: str = Query(None, description = "Mês")):
    async with Client() as client:
        vendas = await client.vendas(ano, mes, True)
        return vendas

@router.put("/vendas", dependencies = [Depends(authenticate)])
async def add_venda(venda: Venda):
    async with Client() as client: 
        await client.add_venda(venda)
        return { "message": 'Venda adicionada com sucesso' }

@router.delete("/vendas", dependencies = [Depends(authenticate)])
async def remove_venda(id: ID):
    async with Client() as client: 
        await client.remove_venda(id)
        return { "message": 'Venda removida com sucesso' }