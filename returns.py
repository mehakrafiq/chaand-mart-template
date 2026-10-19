from datetime import date

# SPEC  can_return(order, today) -> (allowed, reason)
# 1. status must be "delivered"                      else (False, "not delivered yet")
# 2. refunded must be False                          else (False, "already refunded")
# 3. at most 7 days after delivered_on               else (False, "return window closed")
# otherwise (True, "can return"). Day 7 is allowed, day 8 is not.


def can_return(order: dict, today: date) -> tuple[bool, str]:
    raise NotImplementedError("write this from the spec")
