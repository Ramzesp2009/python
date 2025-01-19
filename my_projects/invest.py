def invest(amount, rate, years):
    for i in range(1, years + 1):
        amount = (amount * rate) + amount
        print(f"Year {i}: ${amount:.2f}")

invest(350, .06, 5)
