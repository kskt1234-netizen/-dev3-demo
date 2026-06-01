"""payment 테스트 — calc_vat 하나만 테스트 (커버리지 낮게 유도)."""
from src.payment import calc_vat


def test_calc_vat():
    assert calc_vat(1000, 0.1) == 100
