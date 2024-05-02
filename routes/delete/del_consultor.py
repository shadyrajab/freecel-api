from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from models.apimodels.identify import ID

router = APIRouter()


@router.delete("/consultores")
async def remove_consultor(id: ID, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(client.remove_consultor, user, **{"id": id})
