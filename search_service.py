import sqlite3


def search_orders(status):
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM orders WHERE status = '{status}'")
    return cursor.fetchall()
