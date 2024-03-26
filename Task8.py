# Поэтапная загрузка данных из большого csv-файла
# в указываемую таблицу PostgreSQL с помощью библиотеки Pandas,
# так же указывая тип разделителя и признак наличия наименования колонок в файле;
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
    Get data from CSV and download it to PostgreSQL by chunks
    :return:
    """
    try:
        # размер буфера для чтения и записи данных
        chunksize = 1000
        # разделитель для чтения данных из файла
        delimiter = ','
        # 0 - заголовок, 1 - нет заголовка
        header = 0

        engine = connection_to_postgres()
        csv_path = input('Enter the path to your csv file: ')
        table_name = input('Enter the table name: ')
        pd.read_csv(csv_path)
        # Загрузка данных порционно
        for chunk in pd.read_csv(csv_path, delimiter=delimiter, header=header, chunksize=chunksize):
            chunk.to_sql(table_name, engine, if_exists='append', index=False)

        logger.info('Data was uploaded successfully')
    except Exception as e:
        logger.exception(e)


data_exchange()
# C:\Users\viagunov\Desktop\practice\sample4.csv
# task8
