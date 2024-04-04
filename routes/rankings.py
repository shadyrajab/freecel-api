from fastapi import APIRouter, Query

from client.client import Client
from handler.handler_request import handle_request

router = APIRouter()


@router.get("/rankings")
async def rankings(
    data_inicio: str = Query(..., description="Data Inicial"),
    data_fim: str = Query(..., description="Data Final"),
    equipe: list = Query(None, description="Equipe"),
):
    async with Client() as client:
        return await handle_request(
            client.Ranking,
            data_inicio=data_inicio,
            data_fim=data_fim,
            equipe=equipe,
            venda="~MIGRAÇÃO"
        )
