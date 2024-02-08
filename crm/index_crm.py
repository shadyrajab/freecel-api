import pytz
from datetime import datetime 
from crm.get_crm import get_crm
from crm.update_crm import update_crm
import asyncio

fuso_horario_brasil = pytz.timezone('America/Sao_Paulo')

async def request_crm():
    while True:
        now = datetime.now(fuso_horario_brasil)
        if now.hour == 23 and now.minute == 59:
            print('Função executada')
            dataHoraInicioCarga = f'{now.year}-{now.month}-{now.day} 00:00:00'
            dataHoraFimCarga = f'{now.year}-{now.month}-{now.day} 23:59:00'
            dataframe = get_crm(dataHoraInicioCarga, dataHoraFimCarga)
            update_crm(dataframe)

            print('Função completa')

            await asyncio.sleep(60)
        
        else:
            pass