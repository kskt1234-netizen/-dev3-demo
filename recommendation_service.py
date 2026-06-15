"""
E-commerce recommendation_service.py — contains CONV-MEM-011 violations
for dev3 demo session 2.
"""
from collections import defaultdict
import time


# [VIOLATION] 상품 추천 캐시 — maxsize/TTL 없음, 무한 증가 (CONV-MEM-011)
recommendation_cache = {}


def get_recommendations(user_id: int) -> list[dict]:
    """사용자별 상품 추천 결과를 메모리에 캐싱 (unbounded dict)."""
    if user_id not in recommendation_cache:
        products = _fetch_recommendations(user_id)
        recommendation_cache[user_id] = products   # 삭제 정책 없음
    return recommendation_cache[user_id]


# [VIOLATION] 상품 조회 히스토리 — maxsize 없음 (CONV-MEM-011)
product_view_history: dict[int, list] = defaultdict(list)


def record_product_view(user_id: int, product_id: int) -> None:
    """조회 이력을 메모리에 누적 (unbounded list per user)."""
    product_view_history[user_id].append({
        "product_id": product_id,
        "viewed_at": time.time(),
    })


# [VIOLATION] 검색 로그 — flush/rotate 없이 메모리에 무제한 누적 (CONV-MEM-011)
search_logs: list[dict] = []


def log_search(user_id: int, query: str, result_count: int) -> None:
    """검색 이벤트를 메모리 버퍼에 누적 (무한 증가, clear 없음)."""
    search_logs.append({
        "user_id": user_id,
        "query": query,
        "result_count": result_count,
        "ts": time.time(),
    })


def _fetch_recommendations(user_id: int) -> list[dict]:
    """실제 추천 엔진 호출 — 데모 스텁."""
    return [
        {"product_id": 1001, "score": 0.95, "category": "electronics"},
        {"product_id": 2034, "score": 0.88, "category": "books"},
    ]
