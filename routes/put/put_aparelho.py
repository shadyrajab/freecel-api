from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from params.request_body import UpdateAparelhoParams

router = APIRouter(prefix="/vendas/aparelho", tags=["vendas/aparelho"])


@router.put("/")
async def update_aparelho(
    params: UpdateAparelhoParams, user: str = Depends(authenticate)
):
    params_filtered = {
        key: value for key, value in params.model_dump().items() if value is not None
    }
    async with Client() as client:
        return await handle_request(client.update_aparelho, user, **params_filtered)
