from fastapi import APIRouter, Query

from client.client import Client
from handler import handler_get_request

router = APIRouter(prefix="/rankings", tags=["stats"])


@router.get("/")
async def rankings(
    data_inicio: str = Query(..., description="Data Inicial"),
    data_fim: str = Query(..., description="Data Final"),
    equipe: list = Query(None, description="Equipe"),
):
    async with Client() as client:
        return await handler_get_request(
            client.Ranking,
            data_inicio=data_inicio,
            data_fim=data_fim,
            equipe=equipe,
            venda="~MIGRAÇÃO",
            status="CONCLUÍDO",
        )
