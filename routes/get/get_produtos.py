from fastapi import APIRouter

from client.client import Client
from handler import handler_get_request

router = APIRouter(prefix="/produtos", tags=["produtos"])


@router.get("/")
async def produtos():
    async with Client() as client:
        return await handler_get_request(client.produtos)
