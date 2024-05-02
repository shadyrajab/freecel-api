import logging
import os

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.gzip import GZipMiddleware

from routes.delete import del_consultor, del_movel, del_produto
from routes.get import (
    get_chamadas,
    get_consultores,
    get_migracoes,
    get_movel,
    get_produtos,
    get_rankings,
    get_stats,
    get_utils,
)
from routes.post import post_consultor, post_movel, post_produto, post_simulacao
from routes.put import put_consultor, put_migracao, put_movel, put_produto

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - def %(funcName)s - %(message)s",
)

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)

routes = [
    route.router
    for route in [
        del_consultor,
        del_movel,
        del_produto,
        get_chamadas,
        get_consultores,
        get_migracoes,
        get_movel,
        get_produtos,
        get_rankings,
        get_stats,
        get_utils,
        post_consultor,
        post_movel,
        post_produto,
        post_simulacao,
        put_consultor,
        put_migracao,
        put_movel,
        put_produto,
    ]
]


for route in routes:
    app.include_router(route)


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logging.error(f"Ocorreu um erro na solicitação: {exc}")
    return {
        "status_code": 500,
        "message": "Ocorreu um erro ao atender sua solicitação.",
        "error": str(exc),
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        access_log=False,
    )
