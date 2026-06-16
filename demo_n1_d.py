def get_orders_with_items():
    orders = Order.objects.all()
    for order in orders:
        items = order.item_set.all()  # N+1 쿼리
