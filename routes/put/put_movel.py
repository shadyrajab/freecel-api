from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler import handler_put_request
from params.request_body import UpdateVendaMovelParams

router = APIRouter(prefix="/vendas/movel", tags=["vendas/movel"])


@router.put("/")
async def update_venda_movel(
    params: UpdateVendaMovelParams, user: str = Depends(authenticate)
):
    params_filtered = {
        key: value for key, value in params.model_dump().items() if value is not None
    }
    async with Client() as client:
        return await handler_put_request(
            client.update_venda_movel, user, **params_filtered
        )
