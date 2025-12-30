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


def get_info():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        sql_get_info = "SELECT * FROM tasks"
        cursor.execute(sql_get_info)
        return cursor.fetchall()
    except Error as e:
        print(f"Ошибка получения информации по таблице: {e}")
    finally:
        if conn:
            conn.close()


print(get_info())