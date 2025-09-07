import sqlite3

connect = sqlite3.connect('LMS.db')
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS members (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               firstname TEXT NOT NULL,
               surname TEXT NOT NULL,
               age INTEGER NOT NULL,
               email TEXT NOT NULL UNIQUE )""") 