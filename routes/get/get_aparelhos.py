from fastapi import APIRouter, Query

from client.client import Client
from handler.handler_request import handle_request

router = APIRouter(prefix="/vendas/aparelho", tags=["vendas/aparelho"])


@router.get("/")
async def vendas_aparelho(
    data_inicio: str = Query(..., description="Data Inicial da Consulta"),
    data_fim: str = Query(..., description="Data Final da Consulta"),
    equipe: list = Query(None, description="Equipe"),
    cnpj: str = Query(None, description="CNPJ"),
    uf: list = Query(None, description="UF"),
    adabas: str = Query(None, description="ADABAS"),
    tipo: list = Query(None, description="Tipos de Venda"),
    status: list = Query(None, description="Status da Venda"),
    responsavel: str = Query(None, description="Responsável pela Venda"),
    plano: list = Query(None, description="Planos das Vendas"),
):
    async with Client() as client:
        return await handle_request(
            client.get_aparelhos,
            data_inicio=data_inicio,
            data_fim=data_fim,
            equipe=equipe,
            cnpj=cnpj,
            uf=uf,
            adabas=adabas,
            tipo=tipo,
            status=status,
            responsavel=responsavel,
            plano=plano,
        )
