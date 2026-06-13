"""cart 테스트 — apply_coupon 하나만 테스트 (커버리지 낮게 유도)."""
from src.cart import apply_coupon


def test_apply_coupon():
    assert apply_coupon(1000, 0.2) == 800
