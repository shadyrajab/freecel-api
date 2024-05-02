from fastapi import APIRouter

from utils.variables import CARGOS, EQUIPE, STATUS_VENDA, SUPERVISORES, TIPO_VENDA

router = APIRouter()


@router.get("/utils")
async def utils():
    return {
        "supervisores": SUPERVISORES,
        "equipe": EQUIPE,
        "tipos": TIPO_VENDA,
        "cargos": CARGOS,
        "status": STATUS_VENDA,
    }
