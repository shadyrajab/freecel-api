import pytz
from datetime import datetime 
from crm.get_crm import get_crm
from crm.update_crm import update_crm
import asyncio

fuso_horario_brasil = pytz.timezone('America/Sao_Paulo')

async def request_crm():
    while True:
        now = datetime.now(fuso_horario_brasil)
        if now.hour == 10 and now.minute == 20:
            print('Função executada')
            dataHoraInicioCarga = f'{now.year}-{str(now.month).zfill(2)}-{str(now.day).zfill(2)} 00:00:00'
            dataHoraFimCarga = f'{now.year}-{str(now.month).zfill(2)}-{str(now.day).zfill(2)} 23:59:00'

            print(dataHoraInicioCarga, dataHoraFimCarga)
            dataframe = get_crm(dataHoraInicioCarga, dataHoraFimCarga)
            update_crm(dataframe)

            print('Função completa')

            await asyncio.sleep(60)
        
        else:
            pass