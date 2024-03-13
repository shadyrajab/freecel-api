from fastapi import APIRouter, Depends, Query

from authenticator.jwt import authenticate
from client.client import Client
from models.consultor import Vendedor
from models.identify import ID
from params.request_body import UpdateConsultorParams

router = APIRouter()


@router.get("/consultores", dependencies=[Depends(authenticate)])
async def consultores():
    async with Client() as client:
        consultores = await client.consultores(True)
        return consultores


@router.post("/consultores", dependencies=[Depends(authenticate)])
async def add_consultor(consultor: Vendedor):
    async with Client() as client:
        await client.add_consultor(consultor)
        return {"message": "Consultor adicionado com sucesso"}


@router.delete("/consultores", dependencies=[Depends(authenticate)])
async def remove_consultor(id: ID):
    async with Client() as client:
        await client.remove_consultor(id)
        return {"message": "Consultor removido com sucesso"}


@router.put("/consultores", dependencies=[Depends(authenticate)])
async def update_consultor(params: UpdateConsultorParams):
    async with Client() as client:
        await client.update_consultor(**params.model_dump())
        return {"message": "Consultor atualizado com sucesso"}


@router.get("/consultores/{nome_consultor}", dependencies=[Depends(authenticate)])
async def consultor(
    nome_consultor: str,
    ano: int = Query(None, description="Ano"),
    mes: str = Query(None, description="Mês"),
    display_vendas: bool = Query(None, description="Mostrar vendas"),
):
    nome_consultor = nome_consultor.replace("_", " ").upper()
    async with Client() as client:
        consultor = await client.Consultor(
            nome_consultor, ano, mes, True, display_vendas
        )
        return consultor.to_json()
