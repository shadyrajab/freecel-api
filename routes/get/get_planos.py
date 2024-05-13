from fastapi import APIRouter

from client.client import Client
from handler import handler_get_request

router = APIRouter(prefix="/planos", tags=["planos"])


@router.get("/")
async def planos():
    async with Client() as client:
        return await handler_get_request(client.get_planos)
