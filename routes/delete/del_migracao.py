from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler import handler_delete_request
from models.identify import ID

router = APIRouter(prefix="/migracao", tags=["migração"])


@router.delete("/")
async def remove_migracao(id: ID, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handler_delete_request(client.remove_migracao, user, **{"id": id})
