from fastapi import APIRouter, Depends, Query
from client.instance import client
from fastapi.encoders import jsonable_encoder
from authenticator.jwt import authenticate
from responses.freecel import Freecel

router = APIRouter()

@router.get("/stats", dependencies = [Depends(authenticate)])
def stats(ano: int = Query(None, description = "Ano"), mes: str = Query(None, description = "Mês")):
    freecel = Freecel(client, ano, mes)
    return jsonable_encoder(freecel.to_json())