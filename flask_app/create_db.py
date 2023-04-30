import sqlite3

def create_sqlite():
    """Функция создает бизу данных"""
    conn = sqlite3.connect('database.db')

    conn.execute('CREATE TABLE IF NOT EXISTS record ('
                 'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                 'text TEXT, current_date DATE, '
                 'current_time TIME, '
                 'click_number INTEGER)'
                 )

    print("Таблицы созданы")
    conn.commit()
    conn.close()
    return True
