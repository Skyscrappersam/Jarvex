import sqlite3

conn = sqlite3.connect("jarvex_memory.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memory (
    key TEXT PRIMARY KEY,
    value TEXT
)
""")

conn.commit()


def remember(key, value):
    cursor.execute("""
    INSERT OR REPLACE INTO memory(key, value)
    VALUES (?, ?)
    """, (key, value))
    conn.commit()


def recall(key):
    cursor.execute("""
    SELECT value FROM memory
    WHERE key=?
    """, (key,))

    result = cursor.fetchone()

    if result:
        return result[0]

    return None