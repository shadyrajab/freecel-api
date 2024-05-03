from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from models.migracao import MigracaoRequestModel

router = APIRouter(prefix="/migracao", tags=["migração"])


@router.post("/")
async def add_migracao(venda: MigracaoRequestModel, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(client.add_migracao, user, **{"venda": venda})
