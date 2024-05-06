from fastapi import APIRouter, Query, Request

from client.client import Client
from handler import handler_get_request

router = APIRouter(prefix="/consultores", tags=["consultores"])


@router.get("/")
async def consultores():
    async with Client() as client:
        return await handler_get_request(client.get_consultores)


@router.get("/{nome_consultor}")
async def consultor(
    request: Request,
    data_inicio: str = Query(..., description="Data Inicial"),
    data_fim: str = Query(..., description="Data Final"),
):
    nome_consultor = request.path_params["nome_consultor"].replace("_", " ").upper()

    async with Client() as client:
        return await handler_get_request(
            client.Consultor,
            consultor=nome_consultor,
            data_inicio=data_inicio,
            data_fim=data_fim,
            venda="~MIGRAÇÃO",
            status="CONCLUÍDO",
        )
