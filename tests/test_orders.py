"""orders 테스트 — total_price 하나만 테스트 (커버리지 낮게 유도)."""
from src.orders import total_price


def test_total_price():
    items = [{"price": 100}, {"price": 200}]
    assert total_price(items) == 300
