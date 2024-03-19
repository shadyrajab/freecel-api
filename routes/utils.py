from fastapi import APIRouter
from utils.variables import SUPERVISORES, TIPO_VENDA, EQUIPE, CARGOS, STATUS_VENDA

router = APIRouter()


@router.get("/utils")
async def utils():
    return {
        "supervisores": SUPERVISORES,
        "equipe": EQUIPE,
        "tipos": TIPO_VENDA,
        "cargos": CARGOS,
        "status": STATUS_VENDA
    }