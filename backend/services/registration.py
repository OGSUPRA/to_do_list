from db.database import get_connection

def registration_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    print(f"DEBUG: Registering user: {username}")
    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
    except Exception as e:
        print(f"DEBUG: Database query failed: {e}")
        conn.close()
        return False
    
    rows_updated = cursor.rowcount
    print(f"DEBUG: Updated {rows_updated} rows")
    conn.close()

def user_exists(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 1 FROM users WHERE username = ?
    """, (username,))

    exists = cursor.fetchone() is not None
    conn.close()
    return exists