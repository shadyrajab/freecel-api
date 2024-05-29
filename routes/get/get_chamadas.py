from fastapi import APIRouter, Depends, Query

from authenticator.jwt import authenticate
from vivo.gestao import VivoGestaoChamadas

router = APIRouter(prefix="/chamadas", tags=["chamadas"])


@router.get("/", dependencies=[Depends(authenticate)])
async def chamadas(
    data_inicio: str = Query(..., description="Data Inicial da Consulta"),
    data_fim: str = Query(..., description="Data Final da Consulta"),
    telefone: str = Query(..., description="Número de Telefone"),
    consultor: str = Query(..., description="Nome do Consultor"),
):
    gestao = VivoGestaoChamadas(data_inicio, data_fim, telefone, consultor)
    return gestao.records
