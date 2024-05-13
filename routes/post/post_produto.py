from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler import handler_post_request
from models import Plano

router = APIRouter(prefix="/planos", tags=["planos"])


@router.post("/")
async def add_plano(produto: Plano, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handler_post_request(
            client.add_plano, user, **{"produto": produto}
        )
