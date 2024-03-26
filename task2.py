# Вызов функции, которая возвращает возраст человека по переданной дате рождения;
import logging
from datetime import date

logging.basicConfig(
    level=logging.INFO,
    filename='terminal.log',
    filemode='a',
    format='%(filename)s | %(funcName)s | %(asctime)s | %(levelname)s | %(message)s'
)
logger = logging.getLogger(__name__)


def age_difference() -> None:
    """
    The function that returns you age by your birthday.
    :return:
    """
    try:
        message = 'Specify the date of your birthday in the format dd.mm.yyyy: '
        day, month, year = input(message).split('.')

        birth_date = date(int(year), int(month), int(day))
        current_date = date.today()
        result = current_date.year - birth_date.year
        if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
            result -= 1
        print(result)
        logger.info('Finished successfully.')
    except Exception as e:
        logger.exception(e)


age_difference()
