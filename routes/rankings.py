from fastapi import APIRouter, Depends, Query
from client.client import Client
from fastapi.encoders import jsonable_encoder
from authenticator.jwt import authenticate

router = APIRouter()

@router.get("/rankings", dependencies = [Depends(authenticate)])
def rankings(ano: int = Query(None, description = "Ano"), mes: str = Query(None, description = "Mês")):
    rankings = Client().Ranking(ano, mes, True)
    return jsonable_encoder(rankings.to_json())