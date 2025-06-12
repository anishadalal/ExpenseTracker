import sqlite3

def init_db():
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        description TEXT,
        amount REAL
    )''')
    conn.commit()
    conn.close()

def insert_expense(date, category, description, amount):
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)",
              (date, category, description, amount))
    conn.commit()
    conn.close()

def fetch_expenses():
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("SELECT * FROM expenses ORDER BY date DESC")
    data = c.fetchall()
    conn.close()
    return data
