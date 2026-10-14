# database.py
# Create SQLite and record attendance

import sqlite3
from pathlib import Path

DB_PATH = Path('database') / 'attendance.db'


def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS attendance (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 student_id TEXT,
                 timestamp TEXT,
                 status TEXT
                 )''')
    conn.commit()
    conn.close()
    print(f"[database] Initialized DB at {DB_PATH}")


if __name__ == "__main__":
    init_db()
