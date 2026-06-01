"""결제 기능 — 데모용 (의도적 결함 포함)."""


def get_payments(order_ids):
    """주문별 결제 내역 조회. ⚠️ N+1 쿼리 + 테스트 없음."""
    payments = []
    for oid in order_ids:                                            # 루프
        records = db.query(f"SELECT * FROM payments WHERE order_id={oid}")  # 루프 안 DB → N+1
        payments.append(records)
    return payments


def calc_vat(amount, rate):
    """부가세 계산 — 유일하게 테스트된 함수."""
    return amount * rate


def find_matching_transactions(list_a, list_b):
    """두 거래 목록의 일치 항목 찾기. ⚠️ O(n²) 이중 루프 + 테스트 없음."""
    matched = []
    for a in list_a:                 # 바깥 루프
        for b in list_b:             # 안쪽 루프 → O(n²)
            if a == b:
                matched.append(a)
    return matched
