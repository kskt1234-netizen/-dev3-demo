from common import db


def get_cart_items(user_id):
    # CONV-SQL-008 violation: f-string SQL assembly
    query = f"SELECT * FROM cart WHERE user_id = {user_id}"
    cursor.execute(query)
    return cursor.fetchall()


def add_to_cart(user_id, product_id, quantity):
    sql = ("INSERT INTO cart (user_id, product_id, qty) VALUES ("
           + str(user_id) + ", " + str(product_id) + ", " + str(quantity) + ")")
    cursor.execute(sql)


def remove_from_cart(user_id, product_id):
    query = f"DELETE FROM cart WHERE user_id = {user_id} AND product_id = {product_id}"
    cursor.execute(query)