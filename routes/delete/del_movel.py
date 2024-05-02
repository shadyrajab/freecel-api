from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from models.requestmodels.identify import ID

router = APIRouter(prefix="/vendas", tags=["Vendas"])


@router.delete("/movel")
async def remove_movel(id: ID, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(client.remove_venda, user, **{"id": id})
