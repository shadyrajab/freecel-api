from fastapi import APIRouter, Depends

from authenticator.jwt import authenticate
from client.client import Client
from handler.handler_request import handle_request
from models.identify import ID
from models.produtos import Produto
from params.request_body import UpdateProdutoParams

router = APIRouter()


@router.get("/produtos")
async def produtos():
    async with Client() as client:
        return await handle_request(client.produtos, as_json=True)


@router.post("/produtos")
async def add_produto(produto: Produto, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(client.add_produto, user, **{"produto": produto})


@router.put("/produtos")
async def update_produto(
    params: UpdateProdutoParams, user: str = Depends(authenticate)
):
    params_filtered = {
        key: value for key, value in params.model_dump().items() if value is not None
    }
    async with Client() as client:
        return await handle_request(client.update_produto, user, **params_filtered)


@router.delete("/produtos")
async def remove_produto(id: ID, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(client.remove_produto, user, **{"id": id})
