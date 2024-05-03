from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from models.produtos import Produto

router = APIRouter(prefix="/produtos", tags=["produtos"])


@router.post("/")
async def add_produto(produto: Produto, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(client.add_produto, user, **{"produto": produto})
