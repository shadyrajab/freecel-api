from fastapi import APIRouter

from client.client import Client
from handler.handler_request import handle_request

router = APIRouter()


@router.get("/produtos")
async def produtos():
    async with Client() as client:
        return await handle_request(client.produtos)
