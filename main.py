from fastapi import FastAPI
from routes import consultor, produtos, rankings, stats, vendas
import uvicorn
import os

app = FastAPI()

routes = [
    consultor.router, 
    produtos.router, 
    rankings.router, 
    stats.router, 
    vendas.router
]

for route in routes:
    app.include_router(route)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))