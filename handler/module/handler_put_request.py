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


async def handler_put_request(client_method, user, **kwargs):
    # O que está sendo removido: Venda, Produto, Consultor, etc...
    act = client_method.__name__.split("_")[1].title()
    try:
        await client_method(**kwargs)
        message = f"{act} atualizado(a) com sucesso {user}."
        logging.info(message)
        return JSONResponse(
            content=jsonable_encoder({"message": message, "params": kwargs}),
            status_code=200,
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
