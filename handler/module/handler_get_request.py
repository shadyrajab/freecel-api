import logging

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from utils.functions import jsonfy

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(asctime)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M",
)


async def handler_get_request(client_method, **kwargs):
    try:
        data = await client_method(**kwargs)
        return JSONResponse(
            content=jsonable_encoder(jsonfy(data)),
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
