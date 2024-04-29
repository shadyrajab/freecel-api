from fastapi import APIRouter, File, UploadFile

from pdfhandler.contrato import read_contract_pdf
from pdfhandler.simplifique import read_simplifique_pdf
from pdfhandler.validate import merge_and_validate

router = APIRouter()


@router.post("/simulacao")
async def simulacao(
    simplifique: UploadFile = File(...),
    contrato: UploadFile = File(...),
    visao: UploadFile = File(...),
):
    if not visao.filename.endswith(".xlsx"):
        return {"message": "Formato da visão inválido"}

    for file in [simplifique, contrato]:
        if not file.filename.endswith(".pdf"):
            return {"message": "Formato de arquivo inválido"}

    delta = await read_simplifique_pdf(simplifique)
    termo_complementar, desc_composicao = await read_contract_pdf(contrato)
    validacao = merge_and_validate(desc_composicao, termo_complementar, visao, delta)
    validacao.to_excel("sekiro.xlsx")
    return {"delta": delta}
