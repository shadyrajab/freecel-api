from fastapi import APIRouter, Query

from client.client import Client
from handler import handler_get_request

router = APIRouter(prefix="/vendas/fixa", tags=["vendas/fixa"])


@router.get("/")
async def vendas_fixa(
    data_inicio: str = Query(..., description="Data Inicial da Consulta"),
    data_fim: str = Query(..., description="Data Final da Consulta"),
    equipe: list = Query(None, description="Equipe"),
    vinculo: list = Query(None, description="Vínculo"),
    cnpj: str = Query(None, description="CNPJ"),
    uf: list = Query(None, description="UF"),
    adabas: str = Query(None, description="ADABAS"),
    tipo: list = Query(None, description="Tipos de Venda"),
    status: list = Query(None, description="Status da Venda"),
    responsavel: str = Query(None, description="Responsável pela Venda"),
    plano: list = Query(None, description="Planos das Vendas"),
    n_pedido: list = Query(None, description="Número de pedido"),
):
    async with Client() as client:
        return await handler_get_request(
            client.get_vendas_fixa,
            data_inicio=data_inicio,
            data_fim=data_fim,
            equipe=equipe,
            vinculo=vinculo,
            cnpj=cnpj,
            uf=uf,
            adabas=adabas,
            tipo=tipo,
            status=status,
            responsavel=responsavel,
            plano=plano,
            n_pedido=n_pedido,
        )
