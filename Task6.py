# Вызов процедуры, у которой есть параметр типа CLOB;
import psycopg2
import logging
from os import getenv
from dotenv import load_dotenv, find_dotenv

logging.basicConfig(
    level=logging.INFO,
    filename='terminal.log',
    filemode='a',
    format='%(filename)s | %(funcName)s | %(asctime)s | %(levelname)s | %(message)s'
)
logger = logging.getLogger(__name__)


def call_procedure_clob() -> None:
    """
    The function of calling a procedure(clob parameter)
    :return:
    """
    load_dotenv(find_dotenv())
    conn = psycopg2.connect(
        host=getenv("DB_HOST"),
        port=getenv("DB_PORT"),
        dbname=getenv("DB_NAME"),
        user=getenv("DB_USER"),
        password=getenv("DB_PASSWORD")
    )
    text = input('Enter the text to be stored in the CLOB: ')
    try:
        # Вызов процедуры
        q = conn.cursor()
        logger.info('Connected successfully.')
        q.execute('CALL proctask6clob(%s)', (text,))

        logger.info('Data was uploaded successfully')
        conn.commit()
        conn.close()
    except Exception as e:
        logger.exception(e)


call_procedure_clob()
