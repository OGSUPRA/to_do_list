import sqlite3 as sql
from sqlite3 import Error


def create_connection():
    conn = None
    try:
        conn = sql.connect('pet_project/backend/database.db')
        print("Подключение к SQLite успешно")
    except Error as e:
        print(f'Ошибка подключения: {e}')
    return conn


def delete_task(id_task):
    try: 
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM tasks WHERE id = {id_task}")
        conn.commit()
        print(f"Из таблицы удалина строк с id {id_task}")
    except Error as e:
        print(f"Ошибка при удалении строки с id {id_task}: {e}")
    finally:
        if conn:
            conn.close()


id_task = int(input("Введите id строки, которую необходимо удалить "))
delete_task(id_task)
