from fastapi import APIRouter, Depends, Query

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from models.identify import ID
from models.vendas import Venda
from params.request_body import UpdateVendaParams

router = APIRouter()


@router.get("/vendas")
async def vendas(
    data_inicio: str = Query(..., description="Data Inicial"),
    data_fim: str = Query(..., description="Data Final"),
    equipe: str = Query(None, description="Equipe"),
    cnpj: str = Query(None, description="CNPJ"),
    uf: str = Query(None, description="UF"),
    adabas: str = Query(None, description="ADABAS"),
):
    async with Client() as client:
        return await handle_request(
            client.vendas,
            data_inicio=data_inicio,
            data_fim=data_fim,
            equipe=equipe,
            cnpj=cnpj,
            uf=uf,
            adabas=adabas,
            tipo="MIGRAÇÃO"
        )


@router.post("/vendas")
async def add_venda(venda: Venda, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(client.add_venda, user, **{"venda": venda})


@router.put("/vendas")
async def update_venda(params: UpdateVendaParams, user: str = Depends(authenticate)):
    params_filtered = {
        key: value for key, value in params.model_dump().items() if value is not None
    }
    async with Client() as client:
        return await handle_request(client.update_venda, user, **params_filtered)


@router.delete("/vendas")
async def remove_venda(id: ID, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(client.remove_venda, user, **{"id": id})
