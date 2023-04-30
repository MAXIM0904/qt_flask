from flask import Blueprint, request

from flask_app.db.db import get_db
from flask_app.service.utils import format_dataclass_data, list_dataclass_data


processing = Blueprint("profile", __name__)


@processing.route('/save_data', methods=['POST'])
def save_data():
    """Функция записи информации в базу данных.
    Принимает параметр:
        text - текст введенный пользователем,
        current_date - текущая дата ввода пользователем текста,
        current_time - текущее время ввода пользователем текста,
        click_number - порядковый номер ввода текста.
    """
    try:
        data = format_dataclass_data(request.data)
        cur = get_db().cursor()
        cur.execute("INSERT INTO record(text, current_date, current_time, click_number) VALUES(?, ?, ?, ?)",
                        (data.text, data.current_date, data.current_time, data.click_number))
        get_db().commit()
        return {"answer": "Запись выполнена успешно!"}
    except Exception as err:
        return {"error": f"Ошибка записи! {err}"}
    finally:
        get_db().close()


def _prepare_data(cursor, row: list):
    """Функция преобразует данные из базы в словарь"""
    data = {}
    for index, column in enumerate(cursor.description):
        data[column[0]] = row[index]
    return data


@processing.route('/get_data', methods=['GET'])
def get_data():
    """Функция получает данные из базы и возвращает пользователю"""
    try:
        cur = get_db().cursor()
        cur.row_factory = _prepare_data
        cur.execute("SELECT * FROM record;")
        one_result = list_dataclass_data(cur.fetchall())
        return {"answer": one_result.list_data}
    except Exception as err:
        return {"error": f"Ошибка записи! {err}"}
    finally:
        get_db().close()
