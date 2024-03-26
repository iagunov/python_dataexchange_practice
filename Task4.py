# Вызов процедуры;
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


def call_procedure() -> None:
    """
    The function of calling a procedure
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
        q = conn.cursor()
        logger.info('Connected successfully.')

        q.execute(f"CALL task4procedure()")
        conn.commit()
        conn.close()
        logger.info('The procedure has been called.')
    except Exception as e:
        logger.exception(e)


call_procedure()
