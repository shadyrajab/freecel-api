from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler import handler_delete_request
from models.identify import ID

router = APIRouter(prefix="/vendas/movel", tags=["vendas/movel"])


@router.delete("/")
async def remove_movel(id: ID, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handler_delete_request(
            client.remove_venda_movel, user, **{"id": id}
        )
