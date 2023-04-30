from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QListView
from PyQt6.QtGui import QStandardItemModel, QStandardItem

import requests
import json

from graphical_interface.utils import TextEditor
from graphical_interface.config import url_requests

app = QApplication([])

notes_win = QWidget()
notes_win.setWindowTitle('Графический интерфейс')
notes_win.resize(900, 600)

text_output = QListView()
text_output.setObjectName("Поле для текста")

field_text = QLineEdit('')
field_text.setPlaceholderText('Введите текст...')

button_save_text = QPushButton('Сохранить текст')
button_upload_text = QPushButton('Показать записи')

finished_window = QHBoxLayout()
layout_text_input = QVBoxLayout()

layout_button = QHBoxLayout()
layout_button.addWidget(button_save_text)
layout_button.addWidget(button_upload_text)

layout_text_input.addWidget(text_output)
layout_text_input.addWidget(field_text)
layout_text_input.addLayout(layout_button)


notes_win.setLayout(layout_text_input)


def save_text():
    """Функция записи в базу данных"""
    model = QStandardItemModel()
    text_output.setModel(model)
    tag = field_text.text()
    form_request = dict_request.request_formation(tag)
    response = requests.request("POST", form_request['url'],
                                headers=form_request['headers'],
                                data=form_request['payload'])
    if response.status_code == 200:
        model.appendRow(QStandardItem(f"Данные {form_request['payload']} успешно сохранены"))
    else:
        model.appendRow(QStandardItem("Ошибка сохранения"))


def get_text():
    """Функция получает информацию о всех записях в базе данных и выводит в QListView"""
    model = QStandardItemModel()
    text_output.setModel(model)
    response = requests.request("GET", f"{url_requests}/v1/get_data",
                                headers={},
                                data={})
    data = json.loads(response.text)
    for answer_i in data['answer']:
        model.appendRow(QStandardItem(f"Текст {answer_i['text']}, "
                                      f"Дата заметки {answer_i['current_date'].split()[0]}, "
                                      f"Время заметки {answer_i['current_time'].split()[1]}, "
                                      f"Количество кликов {answer_i['click_number']}"))

dict_request = TextEditor()
button_save_text.clicked.connect(save_text)
button_upload_text.clicked.connect(get_text)

notes_win.show()
app.exec()

if __name__ == '__main__':
    app = QApplication([])
    app.exec()
