from fastapi import APIRouter, Depends, Query

from authenticator.jwt import authenticate
from client.client import Client
from vivo.gestao import VivoGestaoChamadas

router = APIRouter(prefix="/chamadas", tags=["Chamadas"])


@router.get("/", dependencies=[Depends(authenticate)])
async def chamadas(
    data_inicio: str = Query(..., description="Data Inicial da Consulta"),
    data_fim: str = Query(..., description="Data Final da Consulta"),
):
    async with Client() as client:
        consultores = await client.get_equipe_flavio()
        gestao = VivoGestaoChamadas(data_inicio, data_fim, consultores)
        return gestao.records
