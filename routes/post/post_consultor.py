from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from models.requestmodels.consultor import Vendedor

router = APIRouter(prefix="/consultores", tags=["Consultores"])


@router.post("/")
async def add_consultor(consultor: Vendedor, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(
            client.add_consultor, user, **{"consultor": consultor}
        )
