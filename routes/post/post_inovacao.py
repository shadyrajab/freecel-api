from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from models.inovacao import InovacaoRequestModel

router = APIRouter(prefix="/vendas/inovacao", tags=["vendas/inovacao"])


@router.post("/")
async def add_inovacao(venda: InovacaoRequestModel, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(client.add_inovacao, user, **{"venda": venda})
