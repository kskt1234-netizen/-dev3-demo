import sqlite3


def get_order_detail(order_id):
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM orders WHERE id = {order_id}")
    return cursor.fetchone()
