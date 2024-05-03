from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler import handler_post_request
from models import VendaFixaRequestModel

router = APIRouter(prefix="/vendas/fixa", tags=["vendas/fixa"])


@router.post("/")
async def add_venda_fixa(
    venda: VendaFixaRequestModel, user: str = Depends(authenticate)
):
    async with Client() as client:
        return await handler_post_request(
            client.add_venda_fixa, user, **{"venda": venda}
        )
