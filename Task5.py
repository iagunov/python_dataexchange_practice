# Вызов процедуры, у которой есть out-параметр;
import logging
import psycopg2

from os import getenv
from dotenv import load_dotenv, find_dotenv

logging.basicConfig(
    level=logging.INFO,
    filename='terminal.log',
    filemode='a',
    format='%(filename)s | %(funcName)s | %(asctime)s | %(levelname)s | %(message)s'
)
logger = logging.getLogger(__name__)


def call_procedure_out() -> None:
    """
    The function of calling a procedure(out parameter)
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
    try:
        # Вызов процедуры
        q = conn.cursor()
        logger.info('Connected successfully.')

        q.execute('CALL triple(%s)', (5,))
        result = q.fetchone()[0]  # Получение результата из out-параметра
        logger.info('The procedure has been called.')

        print(result)
        conn.commit()
        conn.close()
    except Exception as e:
        logger.exception(e)


call_procedure_out()
