import json
from datetime import datetime
from dataclasses import dataclass


@dataclass
class SaveData:
    """Класс валидации данных введенных пользователем"""
    text: str
    current_date: datetime
    current_time: datetime
    click_number: int


@dataclass
class ListSaveData:
    """Класс валидации данных для передачи пользователю"""
    list_data: list[SaveData]


def convert(data):
    """Функция преобразует полученные параметры в соответствии с требованиями dataclass"""
    str_time = data['current_time'].replace('-', ':')
    str_date = data['current_date']
    data['current_time'] = datetime.strptime(str_time, '%H:%M:%S')
    data['current_date'] = datetime.strptime(str_date, '%Y-%m-%d')
    return data


def format_dataclass_data(table):
    """Функция валидации данных для записи в базу данных"""
    data = json.loads(table)
    data = convert(data)
    return SaveData(**data)

def list_dataclass_data(list_data):
    """Функция валидации данных для передачи пользователю"""
    return ListSaveData(list_data)

