import unicodedata as ud
import logging
import datetime
import re
from typing import Union

from aiogram.types import CallbackQuery, Message, PreCheckoutQuery

latin_letters = {}

logger = logging.getLogger(__name__)


def is_latin(uchr):
    try:
        return latin_letters[uchr]
    except KeyError:
        return latin_letters.setdefault(uchr, 'LATIN' in ud.name(uchr))


def isnt_command(string):
    return True if "/" != string[0] else False


def only_roman_chars(string):
    for e in string:
        if e.isdigit():
            return False

    # Returns true if string contains only latin characters
    # >>> only_roman_chars(u"hôtel lœwe")
    # True
    # >>> only_roman_chars(u"russian: гага")
    # False
    string = f'u{string.strip()}'
    return all(is_latin(uchr)
               for uchr in string
               if uchr.isalpha())


def get_data(string) -> str:
    data = string.split(':')
    return data


def get_order_date(datetime) -> str:
    month_dict = {"01": "января",
                  "02": "февраля",
                  "03": "марта",
                  "04": "апреля",
                  "05": "мая",
                  "06": "июня",
                  "07": "июля",
                  "08": "августа",
                  "09": "сентября",
                  "10": "октября",
                  "11": "ноября",
                  "12": "декабря"}
    try:
        date = datetime.split('T')[0].split('-')
        day = date[2]
        month = month_dict[date[1]]
        year = date[0]
        return ' '.join([day, month, year])
    except Exception as err:
        logger.error(err)
        return "?"


def get_payment_date(timestamp) -> str:
    month_dict = {"01": "января",
                  "02": "февраля",
                  "03": "марта",
                  "04": "апреля",
                  "05": "мая",
                  "06": "июня",
                  "07": "июля",
                  "08": "августа",
                  "09": "сентября",
                  "10": "октября",
                  "11": "ноября",
                  "12": "декабря"}
    try:
        date = str(datetime.datetime.fromtimestamp(int(timestamp[:len(timestamp) - 3]))).split(' ')[0].split('-')
        day = date[2]
        month = month_dict[date[1]]
        year = date[0]
        return ' '.join([day, month, year])
    except Exception as err:
        logger.error(err)
        return "?"


def get_data(string) -> str:
    data = string.split(':')
    return data


def is_phone_correct(string: str) -> bool:
    try:
        if re.match(r'^\d\d \d\d \d\d \d\d \d\d$', string):
            return True
        else:
            return False
    except:
        return False


def is_date_correct(string: str) -> bool:
    try:
        date_of_birth = datetime.datetime.strptime(string, "%d/%m/%Y")
        return True
    except:
        return False


def is_postcode_correct(string: str) -> bool:
    try:
        if re.match(r'^\d{5}$', string):
            return True
        else:
            return False
    except:
        return False


def is_agdref_correct(string: str) -> bool:
    try:
        if re.match(r'^\d+$', string):

            return True
        else:
            return False
    except:
        return False


def is_address_correct(string: str) -> bool:
    return all(is_latin(uchr)
               for uchr in string
               if uchr.isalpha())


def f_user(data: Union[CallbackQuery, Message, PreCheckoutQuery]) -> str:
    """
    Format message for logging
    Show user data
    """
    try:
        return f"id: {data.from_user.id} ({'@' + data.from_user.username if data.from_user.username else ''} {data.from_user.full_name})"
    except Exception as err:
        logger.error(f"Error in f_user: {err}")
        return ""
