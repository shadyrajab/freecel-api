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


async def handler_post_request(client_method, user, **kwargs):
    function_name = client_method.__name__
    try:
        result = await client_method(user, **kwargs)
        logging.info(f"{function_name} params {kwargs} by {user}")
        return JSONResponse(
            content=jsonable_encoder(
                {
                    "status_code": 200,
                    "message": f"Solicitação {function_name} realizada com sucesso",
                    "id": result,
                    "params": kwargs,
                }
            ),
            status_code=200,
        )

    except Exception as e:
        logging.error(f"{function_name} params {kwargs} error: {e}")
        return JSONResponse(
            content=jsonable_encoder(
                {
                    "message": "Ocorreu um erro ao atender sua solicitação",
                    "params": kwargs,
                    "exception": str(e),
                }
            ),
            status_code=500,
        )
