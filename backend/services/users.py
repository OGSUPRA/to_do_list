from db.database import get_connection


def set_user_avatar(user_id, avatar_path):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET avatar_path = ? WHERE id = ?",
        (avatar_path, user_id)
    )

    conn.commit()
    conn.close()


def get_user_avatar(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT avatar_path FROM users WHERE id = ?",
        (user_id,)
    )
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None
    return row["avatar_path"]
