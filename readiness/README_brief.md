# Readiness exercise (homework, due before Session 7)

Part 1, no AI assistant (about 15 minutes)
- From the repo folder run:  python -m pytest -q readiness/tests
- stats.py has three bugs. Fix them until all 3 tests pass.
- Under each fix, write one line: what was wrong.

Part 2, AI assistant allowed
1. Call the Chaand Mart API: <the API address from the class files>/orders.json
2. Count orders per city, and add up amount_pkr for cash-on-delivery orders that are still pending or shipped.
3. Save the result to output/summary.json
4. Push it to a GitHub repo named readiness-<yourname>
5. In the README, explain in your own words what each part of your code does, and what happens if the API is down.
