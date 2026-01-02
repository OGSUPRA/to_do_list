from db.database import get_connection

def create_task(title, description=None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, description) VALUES (?, ?)",
        (title, description)
    )

    conn.commit()
    conn.close()


def get_all_tasks(include_done=True):
    conn = get_connection()
    cursor = conn.cursor()

    if include_done:
        cursor.execute("""
            SELECT * FROM tasks
            WHERE is_deleted = 0
        """)
    else:
        cursor.execute("""
            SELECT * FROM tasks
            WHERE status = 'todo' AND is_deleted = 0
        """)

    tasks = cursor.fetchall()
    conn.close()
    return tasks


def mark_task_done(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tasks
        SET status = 'done'
        WHERE id = ? AND is_deleted = 0
    """, (task_id,))

    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tasks
        SET is_deleted = 1
        WHERE id = ?
    """, (task_id,))

    conn.commit()
    conn.close()
