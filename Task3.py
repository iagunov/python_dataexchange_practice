# Вызов функции, которая возвращает должность, департамент и оклад сотрудника;
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


def get_employee_description() -> None:
    """
    The function of connecting to PostgreSQL and receiving data
    :return:
    """
    table_name = input('Enter the table name:')
    employee_id = input('Enter the employee id:')
    query = (f"""
                  SELECT position_name,
                  department_name,
                  salary
                  FROM {table_name}
                  WHERE id = {employee_id}
    """)

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
        q.execute(query)
        data = q.fetchone()
        conn.close()
        logger.info('The data has been received')
        print(data)
    except Exception as e:
        logger.exception(e)


get_employee_description()
# task3
# 4
