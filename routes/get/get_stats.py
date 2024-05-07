from fastapi import APIRouter, Query

from client.client import Client
from handler import handler_get_request

router = APIRouter(prefix="/stats", tags=["stats"])

STATUS_PARA_CONSTAR_NO_RANKING = ["CONCLUIDO", "FATURANDO-PORTABILIDADE"]


@router.get("/movel")
async def movel(
    data_inicio: str = Query(..., description="Data Inicial"),
    data_fim: str = Query(..., description="Data Final"),
    equipe: str = Query(None, description="Equipe"),
):
    async with Client() as client:
        return await handler_get_request(
            client.Movel,
            data_inicio=data_inicio,
            data_fim=data_fim,
            equipe=equipe,
            status=STATUS_PARA_CONSTAR_NO_RANKING,
        )


@router.get("/fixa")
async def fixa(
    data_inicio: str = Query(..., description="Data Inicial"),
    data_fim: str = Query(..., description="Data Final"),
    equipe: str = Query(None, description="Equipe"),
):
    async with Client() as client:
        return await handler_get_request(
            client.Fixa,
            data_inicio=data_inicio,
            data_fim=data_fim,
            equipe=equipe,
            status=STATUS_PARA_CONSTAR_NO_RANKING,
        )


@router.get("/geral")
async def geral(
    data_inicio: str = Query(..., description="Data Inicial"),
    data_fim: str = Query(..., description="Data Final"),
    equipe: str = Query(None, description="Equipe"),
):
    async with Client() as client:
        return await handler_get_request(
            client.Geral,
            data_inicio=data_inicio,
            data_fim=data_fim,
            equipe=equipe,
            status=STATUS_PARA_CONSTAR_NO_RANKING,
        )
