import sqlite3


def get_user_orders(user_id):
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM orders WHERE user_id = {user_id}")
    return cursor.fetchall()
