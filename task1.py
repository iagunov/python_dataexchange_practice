# Выгрузка данных из указываемой таблицы БД PostgreSQL в json-формате
import json
import psycopg2
import logging
from typing import Any
from os import getenv
from dotenv import load_dotenv, find_dotenv

logging.basicConfig(
    level=logging.INFO,
    filename='terminal.log',
    filemode='a',
    format='%(filename)s | %(funcName)s | %(asctime)s | %(levelname)s | %(message)s'
)
logger = logging.getLogger(__name__)


def get_data_from_postgres(table_name: str) -> list[tuple[Any, ...]]:
    """
    The function of connecting to PostgreSQL and receiving data
    :param table_name:
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

        q.execute(f"SELECT * FROM {table_name}")
        data = q.fetchall()
        conn.close()

        logger.info('The data has been received.')
        return data
    except Exception as e:
        logger.exception(e)


def json_serialize() -> None:
    """
    Data serialization function to JSON
    :return:
    """
    try:
        table_name = input('Enter the table name:')
        data = get_data_from_postgres(table_name)
        json_data = json.dumps(data, default=str)
        logger.info('Serialized successfully.')

        print(json_data)
    except Exception as e:
        logger.exception(e)


json_serialize()
# person
