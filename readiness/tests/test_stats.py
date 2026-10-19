import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))   # so "import stats" finds readiness/stats.py
from stats import average_order_value

ORDERS = [
    {"order_id": 1, "status": "pending", "amount_pkr": 4290},
    {"order_id": 2, "status": "pending", "amount_pkr": 7990},
    {"order_id": 3, "status": "shipped", "amount_pkr": 1890},
    {"order_id": 4, "status": "pending", "amount_pkr": 6293},
]


def test_pending_average():
    assert average_order_value(ORDERS, "pending") == 6191.0


def test_status_nobody_has():
    assert average_order_value(ORDERS, "lost") == 0.0


def test_empty_list():
    assert average_order_value([], "pending") == 0.0
