from fastapi import APIRouter, Depends, Query

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from params.request_body import UpdateMigracaoParams

router = APIRouter()


@router.get("/migracoes")
async def migracoes(
    ano: int = Query(None, description="Ano"), mes: str = Query(None, description="Mês")
):
    async with Client() as client:
        return await handle_request(
            client.vendas, as_json=True, ano=ano, mes=mes, tipo="MIGRAÇÃO"
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
