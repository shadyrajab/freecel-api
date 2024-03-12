from fastapi import APIRouter, Depends, Query
from client.client import Client
from authenticator.jwt import authenticate

router = APIRouter()

@router.get("/stats", dependencies = [Depends(authenticate)])
async def stats(ano: int = Query(None, description = "Ano"), mes: str = Query(None, description = "Mês")):
    async with Client() as client:
        freecel = await client.Freecel(ano, mes, True)
        return freecel.to_json()