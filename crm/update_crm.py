import psycopg2
from dotenv import load_dotenv
from os import getenv

load_dotenv()

HOST = getenv('host')
DATABASE = getenv('database')
USER = getenv('user')
PASSWORD = getenv('password')

def update_crm(dataframe):
    connection = psycopg2.connect(
        host = HOST,
        database = DATABASE,
        user = USER,
        password = PASSWORD
    )

    cursor = connection.cursor()

    cursor.execute('DELETE FROM crm')
    
    for _indice, linha in dataframe.iterrows():
        cursor.execute(f"INSERT INTO crm VALUES (%s);" % ','.join("'" + str(x) + "'" for x in linha))

    connection.commit()

    cursor.close()
    connection.close()
