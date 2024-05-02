from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from models.requestmodels.vendas import Venda

router = APIRouter(prefix="/vendas", tags=["Vendas"])


@router.post("/movel")
async def add_venda(venda: Venda, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(client.add_venda, user, **{"venda": venda})
