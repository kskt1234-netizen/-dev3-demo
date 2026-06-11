"""주문 관련 기능 — 데모용 (의도적 결함 포함)."""


def get_orders(user_ids):
    """유저별 주문 조회. ⚠️ N+1 쿼리 + 테스트 없음."""
    orders = []
    for uid in user_ids:                                        # 루프
        user_orders = db.query(f"SELECT * FROM orders WHERE user_id={uid}")  # 루프 안 DB → N+1
        orders.append(user_orders)
    return orders


def total_price(items):
    """합계 계산 — 유일하게 테스트된 함수."""
    return sum(item["price"] for item in items)


def find_common_items(cart_a, cart_b):
    """두 장바구니의 공통 상품 찾기. ⚠️ O(n²) 이중 루프 + 테스트 없음."""
    common = []
    for a in cart_a:                 # 바깥 루프
        for b in cart_b:             # 안쪽 루프 → O(n²)
            if a == b:
                common.append(a)
    return common
