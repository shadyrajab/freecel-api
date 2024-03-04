from fastapi import APIRouter, Depends, Query
from client.instance import client
from fastapi.encoders import jsonable_encoder
from authenticator.jwt import authenticate
from responses.rankings import Rankings

router = APIRouter()

@router.get("/rankings", dependencies = [Depends(authenticate)])
def rankings(ano: int = Query(None, description = "Ano"), mes: str = Query(None, description = "Mês")):
    rankings = Rankings(client, ano, mes)
    return jsonable_encoder(rankings.to_json())