import sqlite3

DB = "database.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS alerts (
        symbol TEXT PRIMARY KEY,
        triggered INTEGER
    )
    """)

    conn.commit()
    conn.close()


def has_triggered(symbol):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("SELECT triggered FROM alerts WHERE symbol=?", (symbol,))
    row = c.fetchone()

    conn.close()

    return row is not None and row[0] == 1


def set_triggered(symbol, value):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    INSERT INTO alerts(symbol, triggered)
    VALUES (?, ?)
    ON CONFLICT(symbol) DO UPDATE SET triggered=excluded.triggered
    """, (symbol, value))

    conn.commit()
    conn.close()