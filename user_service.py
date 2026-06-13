from database import db

def get_user(user_id: str):
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    return db.execute(query)

def get_orders(status: str):
    query = f"SELECT * FROM orders WHERE status = '{status}'"
    return db.execute(query)
