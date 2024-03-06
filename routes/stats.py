from fastapi import APIRouter, Depends, Query
from client.instance import get_client
from fastapi.encoders import jsonable_encoder
from authenticator.jwt import authenticate

router = APIRouter()

@router.get("/stats", dependencies = [Depends(authenticate)])
def stats(ano: int = Query(None, description = "Ano"), mes: str = Query(None, description = "Mês")):
    freecel = get_client().Freecel(ano, mes, True)
    return jsonable_encoder(freecel.to_json())