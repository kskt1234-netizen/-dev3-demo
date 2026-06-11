"""posts 테스트 — calc_discount 하나만 테스트 (커버리지 낮게 유도)."""
from src.posts import calc_discount


def test_calc_discount():
    assert calc_discount(1000, 0.1) == 900
