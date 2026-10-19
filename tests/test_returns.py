import json
from datetime import date

from returns import can_return

ORDERS = {o["order_id"]: o for o in json.load(open("sample_10.json", encoding="utf-8"))}
TODAY = date(2026, 10, 12)


def test_day_7_after_delivery_can_return():      # 1039 delivered 3 Oct, day 7 = 10 Oct
    assert can_return(ORDERS[1039], date(2026, 10, 10)) == (True, "can return")


def test_day_8_after_delivery_cannot():
    assert can_return(ORDERS[1039], date(2026, 10, 11)) == (False, "return window closed")


def test_not_delivered_cannot_return():
    assert can_return(ORDERS[1001], TODAY) == (False, "not delivered yet")


def test_already_refunded():
    o = dict(ORDERS[1028], refunded=True)
    assert can_return(o, TODAY) == (False, "already refunded")
