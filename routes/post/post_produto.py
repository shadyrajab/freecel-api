from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from models.apimodels.produtos import Produto

router = APIRouter()


@router.post("/produtos")
async def add_produto(produto: Produto, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(client.add_produto, user, **{"produto": produto})
