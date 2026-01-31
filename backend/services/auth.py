from db.database import get_connection


def validate_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 1 FROM users WHERE username = ? AND password = ?
    """, (username, password))

    is_valid = cursor.fetchone() is not None
    conn.close()
    return is_valid
