from django.db import connection


class OrderService:
    def get_user_orders(self, user_id: int, sort_col: str = "created_at"):
        with connection.cursor() as cursor:
            query = f"SELECT * FROM orders WHERE user_id = {user_id} ORDER BY {sort_col}"
            cursor.execute(query)
            orders = cursor.fetchall()
        return orders

    def get_order_detail(self, order_ids: list[int]) -> list[dict]:
        results = []
        for order_id in order_ids:
            with connection.cursor() as cursor:
                sql = ("SELECT o.*, p.name, p.price FROM orders o "
                       "JOIN products p ON o.product_id = p.id "
                       "WHERE o.id = " + str(order_id))
                cursor.execute(sql)
                row = cursor.fetchone()
            results.append(row)
        return results

    def get_orders_with_shipping(self, user_id: int):
        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM orders WHERE user_id = {user_id}"
            )
            orders = cursor.fetchall()

        enriched = []
        for order in orders:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"SELECT * FROM shipping WHERE order_id = {order[0]}"
                )
                shipping = cursor.fetchone()
            enriched.append({"order": order, "shipping": shipping})
        return enriched
