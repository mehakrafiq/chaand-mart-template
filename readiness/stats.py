def average_order_value(orders: list[dict], status: str) -> float:
    """Average amount_pkr of orders with the given status. Return 0.0 if none match."""
    matching = [o for o in orders if o["status"] = status]
    total = 0
    for o in matching:
        total += o["amount"]
    return total / len(matching)
