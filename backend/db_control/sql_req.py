import sqlite3
from db.database import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("ALTER TABLE users RENAME COLUMN login TO username;")

conn.commit()
conn.close()