# Загрузка данных из excel-файла в указываемую таблицу PostgreSQL с помощью библиотеки Pandas;
import pandas as pd
import logging
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from os import getenv
from dotenv import load_dotenv, find_dotenv

logging.basicConfig(
    level=logging.INFO,
    filename='terminal.log',
    filemode='a',
    format='%(filename)s | %(funcName)s | %(asctime)s | %(levelname)s | %(message)s'
)
logger = logging.getLogger(__name__)


def connection_to_postgres() -> Engine:
    """
    PostgreSQL connection
    :return:
    """
    try:
        load_dotenv(find_dotenv())

        DB_NAME = getenv("DB_NAME")
        DB_HOST = getenv("DB_HOST")
        DB_PORT = getenv("DB_PORT")
        DB_USER = getenv("DB_USER")
        DB_PASSWORD = getenv("DB_PASSWORD")

        link = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
        engine = create_engine(link)

        engine.connect()
        logger.info('Connected successfully.')

        return engine
    except Exception as e:
        logger.exception(e)


def data_exchange() -> None:
    """
    Get data from Excel and download it to PostgreSQL
    :return:
    """
    try:
        engine = connection_to_postgres()
        exel_path = input('Enter the path to your exel file: ')
        table_name = input('Enter the table name: ')
        excel_data = pd.read_excel(exel_path)
        excel_data.to_sql(table_name, engine, if_exists='append', index=False)
        logger.info('Data was uploaded successfully')
    except Exception as e:
        logger.exception(e)


data_exchange()
# C:\Users\viagunov\Desktop\test_data.xlsx
# task7
