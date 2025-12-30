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


def pust_info(title, description):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO tasks (title, description) VALUES ('{title}', '{description}')")
        conn.commit()
        print("В таблицу добавлена информация")
    except Error as e:
        print(f"Ошибка записи информации в таблицу {e}")
    finally:
        if conn:
            conn.close()

title = (input("Введите оглавление задачи "))
description = (input("Введите описание задачи "))
pust_info(title, description)
