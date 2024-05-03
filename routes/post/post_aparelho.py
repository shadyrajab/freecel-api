from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_post_request import handler_post_request
from models.aparelho import TrocaAparelhoRequestModel

router = APIRouter(prefix="/vendas/aparelho", tags=["vendas/aparelho"])


@router.post("/")
async def add_aparelho(
    venda: TrocaAparelhoRequestModel, user: str = Depends(authenticate)
):
    async with Client() as client:
        return await handler_post_request(client.add_aparelho, user, **{"venda": venda})
