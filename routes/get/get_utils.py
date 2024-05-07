from fastapi import APIRouter

from utils.utils import (
    EQUIPES,
    ESTEIRA,
    STATUS_FIXA,
    STATUS_MOVEL,
    SUPERVISORES,
    TIPOS_FIXA,
    TIPOS_MIGRACAO,
    TIPOS_MOVEL,
)

router = APIRouter(prefix="/utils", tags=["utils"])


@router.get("/tipos_fixa")
async def tipos_fixa():
    return TIPOS_FIXA


@router.get("/tipo_migracao")
async def tipos_migracao():
    return TIPOS_MIGRACAO


@router.get("/tipos_movel")
async def tipos_movel():
    return TIPOS_MOVEL


@router.get("/supervisores")
async def supervisores():
    return SUPERVISORES


@router.get("/equipes")
async def equipes():
    return EQUIPES


@router.get("/esteira")
async def esteira():
    return ESTEIRA


@router.get("status_fixa")
async def status_fixa():
    return STATUS_FIXA


@router.get("status_movel")
async def status_movel():
    return STATUS_MOVEL
