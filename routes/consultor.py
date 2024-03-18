import logging

from fastapi import APIRouter, Depends, Query

from authenticator.jwt import authenticate
from client.client import Client
from models.consultor import Vendedor
from models.identify import ID
from params.request_body import UpdateConsultorParams

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(
    filename="logs/consultor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s",
)

router = APIRouter()


async def handle_request(client_method, *args, **kwargs):
    function = client_method.__name__
    try:
        result = await client_method(*args, **kwargs)
        logging.info(f"{function} params {kwargs} by {args}")
        if function == "Consultor":
            return result.to_json()

        if function in {"update_consultor", "remove_consultor"}:
            logging.info(f"{function} params {kwargs}")
            return {
                "status_code": 200,
                "message": f"Solicitação realizada com sucesso {function}",
                "params": kwargs,
            }

        return result

    except Exception as e:
        logging.error(f"{function} params {kwargs} error: {e}")
        return {
            "status_code": 500,
            "message": "Ocorreu um erro ao atender sua solicitação",
            "params": kwargs,
            "exception": str(e),
        }


@router.get("/consultores")
async def consultores():
    async with Client() as client:
        return await handle_request(client.consultores, as_json=True)


@router.post("/consultores")
async def add_consultor(consultor: Vendedor, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(client.add_consultor, consultor)


@router.delete("/consultores")
async def remove_consultor(id: ID, user: str = Depends(authenticate)):
    async with Client() as client:
        return await handle_request(client.remove_consultor, id)


@router.put("/consultores")
async def update_consultor(
    params: UpdateConsultorParams, user: str = Depends(authenticate)
):
    params_filtered = {
        key: value for key, value in params.model_dump().items() if value is not None
    }
    async with Client() as client:
        return await handle_request(client.update_consultor, **params_filtered)


@router.get("/consultores/{nome_consultor}")
async def consultor(
    nome_consultor: str,
    ano: int = Query(None, description="Ano"),
    mes: str = Query(None, description="Mês"),
    display_vendas: bool = Query(False, description="Mostrar vendas"),
):
    nome_consultor = nome_consultor.replace("_", " ").upper()
    async with Client() as client:
        return await handle_request(
            client.Consultor,
            nome=nome_consultor,
            ano=ano,
            mes=mes,
            jsonfy=True,
            display_vendas=display_vendas,
        )
