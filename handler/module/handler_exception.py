import logging

from fastapi import Request

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(asctime)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M",
)


async def handler_exception(request: Request, exc: Exception):
    print(request)
    logging.error(f"Ocorreu um erro na solicitação: {exc}")
    return {
        "status_code": 500,
        "message": "Ocorreu um erro ao atender sua solicitação.",
        "error": str(exc),
    }
