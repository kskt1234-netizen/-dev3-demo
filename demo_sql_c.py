def list_orders(sort_by):
    order_col = sort_by  # 사용자 입력 검증 없음
    query = f"SELECT * FROM orders ORDER BY {order_col}"
    cursor.execute(query)
