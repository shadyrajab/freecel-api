import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

from routes import consultor, produtos, rankings, stats, vendas

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)

routes = [
    consultor.router,
    produtos.router,
    rankings.router,
    stats.router,
    vendas.router,
]

for route in routes:
    app.include_router(route)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
