from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from models.apimodels.consultor import Vendedor

router = APIRouter()


@router.post("/consultores")
async def add_consultor(consultor: Vendedor, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(
            client.add_consultor, user, **{"consultor": consultor}
        )
