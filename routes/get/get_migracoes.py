from fastapi import APIRouter, Query

from client.client import Client
from handler.handler_request import handle_request

router = APIRouter(prefix="/migracoes", tags=["migração"])


@router.get("/")
async def migracoes(
    data_inicio: str = Query(..., description="Ano"),
    data_fim: str = Query(..., description="Mês"),
):
    async with Client() as client:
        return await handle_request(
            client.get_migracoes,
            data_inicio=data_inicio,
            data_fim=data_fim,
        )
