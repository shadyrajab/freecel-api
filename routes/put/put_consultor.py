from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler import handler_put_request
from params.request_body import UpdateConsultorParams

router = APIRouter(prefix="/consultores", tags=["consultores"])


@router.put("/")
async def update_consultor(
    params: UpdateConsultorParams, user: str = Depends(authenticate)
):
    params_filtered = {
        key: value for key, value in params.model_dump().items() if value is not None
    }
    async with Client() as client:
        return await handler_put_request(
            client.update_consultor, user, **params_filtered
        )
