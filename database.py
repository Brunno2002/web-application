import sqlite3 as sq

def create_data():
    con = sq.connect("data/students_database.db")
    cur = con.cursor()
    db = cur.execute("""CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password_hash TEXT NOT NULL,
                    create_at DATETIME DEFAULT CURRENT_TIMESPAMP,
                    last_login DATETIME
                    )""")

