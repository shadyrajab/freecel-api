from fastapi import APIRouter, Depends, Query

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from params.request_body import UpdateMigracaoParams

router = APIRouter()


@router.get("/migracoes")
async def migracoes(
    data_inicio: str = Query(..., description="Ano"),
    data_fim: str = Query(..., description="Mês"),
):
    async with Client() as client:
        return await handle_request(
            client.vendas,
            data_inicio=data_inicio,
            data_fim=data_fim,
            tipo="MIGRAÇÃO",
        )


@router.put("/migracoes")
async def update_migracao(
    params: UpdateMigracaoParams, user: str = Depends(authenticate)
):
    params_filtered = {
        key: value for key, value in params.model_dump().items() if value is not None
    }
    async with Client() as client:
        return await handle_request(client.update_venda, user, **params_filtered)
