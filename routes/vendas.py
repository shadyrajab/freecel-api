from fastapi import APIRouter, Depends, Query

from authenticator.jwt import authenticate
from client.client import Client
from models.identify import ID
from models.vendas import Venda

router = APIRouter()


@router.get("/vendas", dependencies=[Depends(authenticate)])
async def vendas(
    ano: int = Query(None, description="Ano"), mes: str = Query(None, description="Mês")
):
    async with Client() as client:
        vendas = await client.vendas(as_json=True, ano=ano, mes=mes)
        return vendas


# @router.get("/vendas/{cnpj}", dependencies = [Depends(authenticate)])
# async def vendas(cnpj: str = Query(description="O CNPJ do cliente")):
#     async with Client() as client:


@router.post("/vendas", dependencies=[Depends(authenticate)])
async def add_venda(venda: Venda):
    async with Client() as client:
        await client.add_venda(venda)
        return {"message": "Venda adicionada com sucesso"}


@router.delete("/vendas", dependencies=[Depends(authenticate)])
async def remove_venda(id: ID):
    async with Client() as client:
        await client.remove_venda(id)
        return {"message": "Venda removida com sucesso"}
