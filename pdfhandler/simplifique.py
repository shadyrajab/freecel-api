import io

from PyPDF2 import PdfReader


async def read_simplifique_pdf(simplifique):
    reader = PdfReader(io.BytesIO(await simplifique.read()))
    extracted_text = reader.pages[1].extract_text().split("\n")

    faturamento_atual = extracted_text[4].replace("Fat.", "").replace(",", ".")
    faturamento_remun = extracted_text[7].replace("Rec.", "").replace(",", ".")
    delta = float(faturamento_atual) - float(faturamento_remun)

    return delta
