import json
from PyQt6.QtCore import QDate, QTime, QDateTime, Qt

from graphical_interface.config import url_requests



class TextEditor:
    """Класс подготовки данные для request"""
    click = 0

    def request_formation(self, text):
        self.click += 1
        time = QTime.currentTime()
        now = QDate.currentDate()
        request_body = {
            "url": f"{url_requests}/v1/save_data",
            "payload": json.dumps({
                "text": text,
                "current_date": now.toString(Qt.DateFormat.ISODate),
                'current_time': time.toString(Qt.DateFormat.ISODate),
                "click_number": self.click
            }),
            "headers": {
                'Content-Type': 'application/json'
            }
        }
        return request_body
