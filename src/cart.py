"""장바구니 기능 — 데모용 (의도적 결함 포함)."""


def load_cart_items(cart_ids):
    """장바구니별 담긴 상품 조회. ⚠️ N+1 쿼리 + 테스트 없음."""
    items = []
    for cid in cart_ids:                                          # 루프
        cart_items = db.query(f"SELECT * FROM cart_items WHERE cart_id={cid}")  # 루프 안 DB → N+1
        items.append(cart_items)
    return items


def apply_coupon(price, discount_rate):
    """쿠폰 적용가 — 유일하게 테스트된 함수."""
    return price * (1 - discount_rate)


def find_duplicate_products(cart):
    """장바구니 내 중복 상품 찾기. ⚠️ O(n²) 이중 루프 + 테스트 없음."""
    dups = []
    for i in cart:                   # 바깥 루프
        for j in cart:               # 안쪽 루프 → O(n²)
            if i == j:
                dups.append(i)
    return dups
