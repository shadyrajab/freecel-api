from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from models.chamadas import Chamada

router = APIRouter()


@router.get("/chamadas")
async def chamadas():
    async with Client() as client:
        return await handle_request(client.chamadas, as_json=True)


@router.post("/chamadas")
async def add_chamada(chamada: Chamada, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(client.add_chamada, user, **{"chamada": chamada})
