from common import db


def get_cart_items(user_id):
    # CONV-SQL-008 위반: f-string SQL 조립
    query = f"SELECT * FROM cart WHERE user_id = {user_id}"
    cursor.execute(query)
    return cursor.fetchall()


def add_to_cart(user_id, product_id, quantity):
    sql = ("INSERT INTO cart (user_id, product_id, qty) VALUES ("
           + str(user_id) + ", " + str(product_id) + ", " + str(quantity) + ")")
    cursor.execute(sql)
