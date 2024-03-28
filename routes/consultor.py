from fastapi import APIRouter, Depends, Query

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from models.consultor import Vendedor
from models.identify import ID
from params.request_body import UpdateConsultorParams

router = APIRouter()


@router.get("/consultores")
async def consultores():
    async with Client() as client:
        return await handle_request(client.consultores)


@router.post("/consultores")
async def add_consultor(consultor: Vendedor, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(
            client.add_consultor, user, **{"consultor": consultor}
        )


@router.delete("/consultores")
async def remove_consultor(id: ID, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(client.remove_consultor, user, **{"id": id})


@router.put("/consultores")
async def update_consultor(
    params: UpdateConsultorParams, user: str = Depends(authenticate)
):
    params_filtered = {
        key: value for key, value in params.model_dump().items() if value is not None
    }
    async with Client() as client:
        return await handle_request(client.update_consultor, user, **params_filtered)


@router.get("/consultores/{nome_consultor}")
async def consultor(
    consultor: str = Query(..., description="Consultor"),
    data_inicio: str = Query(..., description="Data Inicial"),
    data_fim: str = Query(..., description="Data Final"),

):
    nome = consultor.replace("_", " ").upper()
    async with Client() as client:
        return await handle_request(
            client.Consultor,
            consultor=nome,
            data_inicio=data_inicio,
            data_fim=data_fim,
            tipo="~MIGRAÇÃO"
        )
