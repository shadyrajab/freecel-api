from fastapi import APIRouter

from client.client import Client
from handler.handler_request import handle_request

router = APIRouter()


@router.get("/chamadas")
async def chamadas():
    async with Client() as client:
        return await handle_request(client.chamadas, as_json=True)
