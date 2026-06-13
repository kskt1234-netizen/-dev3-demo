"""inventory 테스트 — apply_safety_margin 하나만 테스트 (커버리지 낮게 유도).

7개 함수 중 1개만 테스트 → m3 커버리지 미충족(TEST-001) + 나머지 6개 테스트 누락(TEST-004) 탐지 유도.
"""
import pytest

from src.inventory import apply_safety_margin


def test_apply_safety_margin_basic():
    assert apply_safety_margin(100, 0.2) == 120


def test_apply_safety_margin_rejects_negative():
    with pytest.raises(ValueError):
        apply_safety_margin(-1, 0.2)
