import logging
import os

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.gzip import GZipMiddleware

from routes import consultor, migracoes, produtos, rankings, stats, utils, vendas

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - def %(funcName)s - %(message)s",
)

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)

routes = [
    consultor.router,
    produtos.router,
    rankings.router,
    stats.router,
    vendas.router,
    migracoes.router,
    utils.router
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
