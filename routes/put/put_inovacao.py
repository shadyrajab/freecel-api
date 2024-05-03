from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler import handler_put_request
from params.request_body import UpdateInovacaoParams

router = APIRouter(prefix="/vendas/inovacao", tags=["vendas/inovacao"])


@router.put("/")
async def update_inovacao(
    params: UpdateInovacaoParams, user: str = Depends(authenticate)
):
    params_filtered = {
        key: value for key, value in params.model_dump().items() if value is not None
    }
    async with Client() as client:
        return await handler_put_request(
            client.update_inovacao, user, **params_filtered
        )
