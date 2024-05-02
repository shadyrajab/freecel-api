from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from params.request_body import UpdateConsultorParams

router = APIRouter()


@router.put("/consultores")
async def update_consultor(
    params: UpdateConsultorParams, user: str = Depends(authenticate)
):
    params_filtered = {
        key: value for key, value in params.model_dump().items() if value is not None
    }
    async with Client() as client:
        return await handle_request(client.update_consultor, user, **params_filtered)
