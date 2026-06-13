"""재고 관리 기능 — 데모용 (의도적 결함 포함, 종합판).

기존 데모 브랜치(cart/orders/payment/posts)보다 결함을 더 크게 잡았다:
  - N+1 쿼리
  - O(n³) 삼중 루프 (기존 O(n²)보다 심각)
  - 메모리 누수 2종 (전역 컬렉션 무한 증가 + 파일 핸들 미닫힘)
  - 엣지케이스 미처리 함수 다수 (0·음수·빈값·None)
  - 함수 7개 중 단 1개만 테스트 → 커버리지 대폭 미달
"""


def fetch_stock_levels(product_ids):
    """상품별 재고 조회. ⚠️ N+1 쿼리 + 테스트 없음."""
    levels = []
    for pid in product_ids:                                              # 루프
        stock = db.query(f"SELECT qty FROM stock WHERE product_id={pid}")  # 루프 안 DB → N+1
        levels.append(stock)
    return levels


def find_triple_outages(products):
    """동시에 품절되는 상품 3개 조합 찾기. ⚠️ O(n³) 삼중 루프 + 테스트 없음."""
    outages = []
    for a in products:                  # 바깥 루프
        for b in products:              # 중간 루프
            for c in products:          # 안쪽 루프 → O(n³)
                if a.qty == 0 and b.qty == 0 and c.qty == 0:
                    outages.append((a, b, c))
    return outages


_AUDIT_LOG = []


def record_restock(event):
    """입고 이벤트 기록. ⚠️ 전역 리스트 무한 증가(메모리 누수) + 테스트 없음."""
    _AUDIT_LOG.append(event)            # 전역 컬렉션 무한 append → 메모리 누수
    return len(_AUDIT_LOG)


def export_report(path, rows):
    """재고 리포트 파일 출력. ⚠️ 파일 핸들 미닫힘(메모리/리소스 누수) + 테스트 없음."""
    open(path, "w")                     # with/대입 없이 단독 open() → 핸들 누수
    for row in rows:
        pass
    return path


def calc_reorder_amount(current_qty, threshold):
    """재주문 수량 계산. ⚠️ 음수·0 엣지케이스 미처리 + 테스트 없음."""
    return threshold - current_qty      # current_qty 음수면 과대 주문, threshold 0이면 음수 반환


def average_daily_usage(usages):
    """일평균 사용량. ⚠️ 빈 리스트 미처리(ZeroDivisionError) + 테스트 없음."""
    return sum(usages) / len(usages)    # usages 빈값이면 division by zero


def apply_safety_margin(qty, rate):
    """안전 재고 가산 — 유일하게 테스트된 함수."""
    if qty < 0 or rate < 0:
        raise ValueError("qty and rate must be non-negative")
    return qty * (1 + rate)
