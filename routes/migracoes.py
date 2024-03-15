from fastapi import APIRouter, Depends, Query

from authenticator.jwt import authenticate
from client.client import Client

router = APIRouter()


@router.get("/migracoes", dependencies=[Depends(authenticate)])
async def migracoes(
    ano: int = Query(None, description="Ano"), mes: str = Query(None, description="Mês")
):
    async with Client() as client:
        migracoes = await client.vendas(as_json=True, ano=ano, mes=mes, ja_cliente=True)
        return migracoes
