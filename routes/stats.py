from fastapi import APIRouter, Query

from client.client import Client
from handler.handler_request import handle_request

router = APIRouter()


@router.get("/stats")
async def stats(
    ano: int = Query(None, description="Ano"),
    mes: str = Query(None, description="Mês"),
    equipe: str = Query(None, description="Equipe"),
):
    async with Client() as client:
        return await handle_request(
            client.Freecel, ano=ano, mes=mes, equipe=equipe, jsonfy=True
        )
