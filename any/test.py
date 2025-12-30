import sqlite3
from sqlite3 import Error

def create_connection():
    """Создаём подключение к SQLite базе данных"""
    conn = None
    try:
        conn = sqlite3.connect('database.db')
        print("Подключение к SQLite успешно")
    except Error as e:
        print(f"Ошибка подключения: {e}")
    return conn

def create_table():
    """Создаём таблицу tasks если её нет"""
    conn = create_connection()
    
    sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        is_done BOOLEAN NOT NULL DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    
    try:
        cursor = conn.cursor()
        cursor.execute(sql_create_tasks_table)
        conn.commit()
        print("Таблица 'tasks' создана или уже существует")
    except Error as e:
        print(f"Ошибка создания таблицы: {e}")
    finally:
        if conn:
            conn.close()

# Запускаем создание таблицы при импорте
create_table()