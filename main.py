from fastapi import FastAPI, Query, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.encoders import jsonable_encoder
from client.client import Freecel
import os

import uvicorn

from responses import (
    Consultor, 
    Freecel, 
    get_consultores, 
    Rankings,
    add_consultor_to_db,
    get_vendas,
    add_venda_to_db,
    add_produto_to_db,
    get_produtos,
    token_authenticate,
    remove_venda_from_db,
    remove_produto_from_db,
    remove_consultor_from_db
)

from .types.base_model import (
    ConsultorModel,
    VendaModel,
    ProdutoModel,
    IdentifyModel
)
def markdown_as_a_file():
    with open('home.md', 'r') as md:
        markdown = md.read()

    return markdown

app = FastAPI(
    title = 'Freecel API',
    description = markdown_as_a_file()
)
security = HTTPBearer()

def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials:
        token = credentials.credentials
        print('def_authenticate_token ' + token)
        if token_authenticate(token):
            print('yes if authenticate')
            return True

    raise HTTPException(status_code=401, detail="Autenticação necessária")

@app.get("/stats", dependencies = [Depends(authenticate)])
def stats(
        ano: int = Query(None, description = "Ano (opcional)"), 
        mes: str = Query(None, description = "Mês (opcional)")
    ):

    freecel = Freecel(ano, mes)

    return jsonable_encoder(freecel)

@app.get("/vendas", dependencies = [Depends(authenticate)])
def vendas(
    ano: int = Query(None, description = "Ano (opcional)"), 
    mes: str = Query(None, description = "Mês (opcional)")
):
    return jsonable_encoder(get_vendas(ano, mes))

@app.put("/vendas", dependencies = [Depends(authenticate)])
def add_venda(venda: VendaModel):
    add_venda_to_db(venda)
    
    return { "message": 'Venda adicionada com sucesso' }

@app.delete("/vendas", dependencies = [Depends(authenticate)])
def remove_venda(id: IdentifyModel):
    remove_venda_from_db(id)

    return { "message": 'Venda removida com sucesso' }

@app.get("/produtos", dependencies = [Depends(authenticate)])
def produtos():
    return jsonable_encoder(get_produtos())

@app.put("/produtos", dependencies = [Depends(authenticate)])
def add_produto(produto: ProdutoModel):
    add_produto_to_db(produto)

    return { "message": "Produto adicionado com sucesso" }

@app.delete("/produtos", dependencies = [Depends(authenticate)])
def remove_produto(id: IdentifyModel):
    remove_produto_from_db(id)

    return { "message": 'Produto removido com sucesso' }

@app.get("/consultores", dependencies = [Depends(authenticate)])
def consultores():
    return jsonable_encoder(get_consultores())

@app.put("/consultores", dependencies = [Depends(authenticate)])
def add_consultor(consultor: ConsultorModel):
    add_consultor_to_db(consultor)

    return { 'message': 'Consultor adicionado com sucesso'}

@app.delete("/consultores", dependencies = [Depends(authenticate)])
def remove_consultor(id: IdentifyModel):
    remove_consultor_from_db(id)

    return { "message": 'Consultor removido com sucesso' }

@app.get("/consultores/{nome_consultor}", dependencies = [Depends(authenticate)])
def consultor(
        nome_consultor: str,
        display_vendas: bool = Query(None, description = 'Mostrar vendas (opcional)'), 
        ano: int = Query(None, description = "Ano (opcional)"), 
        mes: str = Query(None, description = "Mês (opcional)")
    ):

    nome_consultor = nome_consultor.replace('_', ' ').upper()
    consultor = Consultor(nome_consultor, display_vendas, ano, mes)

    return jsonable_encoder(consultor)

@app.get("/rankings", dependencies = [Depends(authenticate)])
def rankings(
    ano: int = Query(None, description = "Ano (opcional)"), 
    mes: str = Query(None, description = "Mês (opcional)")
):
    rankings = Rankings(ano, mes)

    return jsonable_encoder(rankings)

# @app.get('/crm')
# def crm():
#     return Crm

# def run_periodic_request():
#     asyncio.set_event_loop(asyncio.new_event_loop())
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(request_crm())

if __name__ == "__main__":
    # thread = threading.Thread(target=run_periodic_request)
    # thread.start()
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))