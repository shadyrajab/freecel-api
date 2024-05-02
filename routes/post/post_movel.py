from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from models.movel import VendaMovelRequestModel

router = APIRouter(prefix="/vendas/movel", tags=["vendas/movel"])


@router.post("/")
async def add_venda_movel(venda: VendaMovelRequestModel, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(client.add_venda, user, **{"venda": venda})
