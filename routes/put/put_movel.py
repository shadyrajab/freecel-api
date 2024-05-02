from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from models.apimodels.identify import ID
from models.apimodels.vendas import Venda
from params.request_body import UpdateVendaParams

router = APIRouter(prefix="/vendas", tags=["Vendas"])


@router.put("/movel")
async def update_venda(params: UpdateVendaParams, user: str = Depends(authenticate)):
    params_filtered = {
        key: value for key, value in params.model_dump().items() if value is not None
    }
    async with Client() as client:
        return await handle_request(client.update_venda, user, **params_filtered)
