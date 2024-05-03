from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler import handler_post_request
from models import TrocaAparelhoRequestModel

router = APIRouter(prefix="/vendas/aparelho", tags=["vendas/aparelho"])


@router.post("/")
async def add_aparelho(
    venda: TrocaAparelhoRequestModel, user: str = Depends(authenticate)
):
    async with Client() as client:
        return await handler_post_request(client.add_aparelho, user, **{"venda": venda})
