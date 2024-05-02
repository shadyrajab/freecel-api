from fastapi import APIRouter, File, UploadFile

from pdfhandler.contrato import read_contract_pdf
from pdfhandler.simplifique import read_simplifique_pdf
from pdfhandler.visao import read_visao_pdf
from utils.functions import jsonfy

router = APIRouter()


@router.post("/simulacao")
async def simulacao(
    simplifique: UploadFile = File(...),
    contrato: UploadFile = File(...),
    visao: UploadFile = File(...),
):

    for file in [simplifique, contrato, visao]:
        if not file.filename.endswith(".pdf"):
            return {"message": "Formato de arquivo inválido"}

    delta = await read_simplifique_pdf(simplifique)
    termo_complementar, desc_composicao = await read_contract_pdf(contrato)
    visao_cliente = await read_visao_pdf(visao)
    return {
        "delta": delta,
        "termo_complementar": jsonfy(termo_complementar),
        "desc_composicao": jsonfy(desc_composicao),
        "visao_cliente": jsonfy(visao_cliente),
    }
