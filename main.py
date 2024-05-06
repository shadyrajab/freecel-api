import logging
import os

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.gzip import GZipMiddleware

from handler import handler_exception
from routes import routes

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - def %(funcName)s - %(message)s",
)

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)


for route in routes:
    app.include_router(route)


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    return await handler_exception(request, exc)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        access_log=False,
    )
