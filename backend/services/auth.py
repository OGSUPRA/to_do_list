from db.database import get_connection

def authenticate_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    print(f"DEBUG: Authenticate user: {username}")

    try:
        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        )
    except Exception as e:
        print(f"DEBUG: Database query failed: {e}")
        conn.close()
        return False
    
    user = cursor.fetchone()
    conn.close()

    if user:
        print("DEBUG: Authentication successful")
        return True
    else:
        print("DEBUG: Authentication failed")
        return False