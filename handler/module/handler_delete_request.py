import logging

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(asctime)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M",
)


async def handler_delete_request(client_method, user: str, **kwargs: dict):
    id = kwargs.get("id")

    # O que está sendo removido: Venda, Produto, Consultor, etc...
    act = client_method.__name__.split("-")[1].title()
    try:
        await client_method(id)
        message = f"{act} de ID {id} removido(a) com sucesso por {user}."
        logging.info(message)
        return JSONResponse(
            content=jsonable_encoder({"message": message}), status_code=200
        )
    except Exception as e:
        message = f"Erro interno. Por favor contate um administrador."
        return JSONResponse(
            content=jsonable_encoder(
                {
                    "message": message,
                    "exception": str(e),
                    "params": kwargs,
                }
            ),
            status_code=500,
        )
