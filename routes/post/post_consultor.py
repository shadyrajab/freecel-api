from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler import handler_get_request
from models.consultor import Vendedor

router = APIRouter(prefix="/consultores", tags=["consultores"])


@router.post("/")
async def add_consultor(consultor: Vendedor, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handler_get_request(
            client.add_consultor, user, **{"consultor": consultor}
        )
