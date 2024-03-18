from fastapi import APIRouter, Depends, Query

from authenticator.jwt import authenticate
from client.client import Client
from params.request_body import UpdateMigracaoParams

router = APIRouter()


@router.get("/migracoes", dependencies=[Depends(authenticate)])
async def migracoes(
    ano: int = Query(None, description="Ano"), mes: str = Query(None, description="Mês")
):
    async with Client() as client:
        migracoes = await client.vendas(as_json=True, ano=ano, mes=mes, tipo="MIGRAÇÃO")
        return migracoes


@router.put("/migracoes", dependencies=[Depends(authenticate)])
async def update_migracao(params: UpdateMigracaoParams):
    async with Client() as client:
        await client.update_venda(**params.model_dump())
        return {"message": "Venda atualizada com sucesso"}
