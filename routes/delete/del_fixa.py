from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler import handler_delete_request
from models import ID

router = APIRouter(prefix="/vendas/fixa", tags=["vendas/fixa"])


@router.delete("/")
async def remove_fixa(id: ID, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handler_delete_request(
            client.remove_venda_fixa, user, **{"id": id}
        )
