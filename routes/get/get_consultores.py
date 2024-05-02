from fastapi import APIRouter, Query, Request

from client.client import Client
from handler.handler_request import handle_request

router = APIRouter()


@router.get("/consultores")
async def consultores():
    async with Client() as client:
        return await handle_request(client.consultores)


@router.get("/consultores/{nome_consultor}")
async def consultor(
    request: Request,
    data_inicio: str = Query(..., description="Data Inicial"),
    data_fim: str = Query(..., description="Data Final"),
):
    nome_consultor = request.path_params["nome_consultor"].replace("_", " ").upper()
    
    async with Client() as client:
        return await handle_request(
            client.Consultor,
            consultor=nome_consultor,
            data_inicio=data_inicio,
            data_fim=data_fim,
            venda="~MIGRAÇÃO",
            status="CONCLUÍDO",
        )
