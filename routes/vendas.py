from fastapi import APIRouter, Depends, Query

from authenticator.jwt import authenticate
from client.client import Client
from models.identify import ID
from models.vendas import Venda
from params.request_body import UpdateVendaParams

router = APIRouter()


@router.get("/vendas", dependencies=[Depends(authenticate)])
async def vendas(
    ano: int = Query(None, description="Ano"),
    mes: str = Query(None, description="Mês"),
    cnpj: str = Query(None, description="CNPJ"),
    uf: str = Query(None, description="UF"),
    adabas: str = Query(None, description="ADABAS"),
):
    async with Client() as client:
        vendas = await client.vendas(
            as_json=True, ano=ano, mes=mes, cnpj=cnpj, uf=uf, adabas=adabas
        )
        return vendas


@router.post("/vendas", dependencies=[Depends(authenticate)])
async def add_venda(venda: Venda):
    async with Client() as client:
        await client.add_venda(venda)
        return {"message": "Venda adicionada com sucesso"}


@router.put("/vendas", dependencies=[Depends(authenticate)])
async def update_venda(params: UpdateVendaParams):
    async with Client() as client:
        await client.update_venda(**params.model_dump())
        return {"message": "Venda atualizada com sucesso"}

@router.delete("/vendas", dependencies=[Depends(authenticate)])
async def remove_venda(id: ID):
    async with Client() as client:
        await client.remove_venda(id)
        return {"message": "Venda removida com sucesso"}
