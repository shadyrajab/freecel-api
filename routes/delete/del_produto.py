from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from models.identify import ID

router = APIRouter(prefix="/produtos", tags=["Produtos"])


@router.delete("/")
async def remove_produto(id: ID, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(client.remove_produto, user, **{"id": id})
