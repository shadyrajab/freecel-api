from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler import handler_post_request
from models import Produto

router = APIRouter(prefix="/produtos", tags=["produtos"])


@router.post("/")
async def add_produto(produto: Produto, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handler_post_request(
            client.add_produto, user, **{"produto": produto}
        )
