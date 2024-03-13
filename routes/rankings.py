from fastapi import APIRouter, Depends, Query

from authenticator.jwt import authenticate
from client.client import Client

router = APIRouter()


@router.get("/rankings", dependencies=[Depends(authenticate)])
async def rankings(
    ano: int = Query(None, description="Ano"), mes: str = Query(None, description="Mês")
):
    async with Client() as client:
        rankings = await client.Ranking(ano, mes, True)
        return rankings.to_json()
