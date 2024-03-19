from fastapi import APIRouter, Query

from client.client import Client
from handler.handler_request import handle_request

router = APIRouter()


@router.get("/rankings")
async def rankings(
    ano: int = Query(None, description="Ano"), mes: str = Query(None, description="Mês")
):
    async with Client() as client:
        return await handle_request(client.Ranking, ano=ano, mes=mes, jsonfy=True)
