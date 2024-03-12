from typing import Optional

from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client

router = APIRouter()


@router.get("/leads", dependencies=[Depends(authenticate)])
async def leads(regiao: Optional[str] = None):
    async with Client() as client:
        pass
