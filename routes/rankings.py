from fastapi import APIRouter, Depends, Query
from client.client import Client
from authenticator.jwt import authenticate

router = APIRouter()

@router.get("/rankings", dependencies = [Depends(authenticate)])
async def rankings(ano: int = Query(None, description = "Ano"), mes: str = Query(None, description = "Mês")):
    async with Client() as client:
        rankings = await client.Ranking(ano, mes, True)
        return await rankings.to_json()