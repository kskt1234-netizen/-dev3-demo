from models import Order, Product

def get_order_details(order_ids: list):
    orders = []
    for order_id in order_ids:
        order = Order.objects.get(id=order_id)
        product = Product.objects.get(id=order.product_id)
        orders.append({"order": order, "product": product})
    return orders
