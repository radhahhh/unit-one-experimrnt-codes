bills = []
n = int(input("Enter number of months: "))

for i in range(n):
    units = float(input("Enter units consumed: "))

    if units < 0:
        print("Invalid units")
        continue

    if units <= 100:
        amount = units * 3
    elif units <= 200:
        amount = 100 * 3 + (units - 100) * 5
    else:
        amount = 100 * 3 + 100 * 5 + (units - 200) * 8

    amount = amount + 50

    if units > 300:
        amount = amount + amount * 0.05

    if units <= 100:
        amount = amount - amount * 0.10

    bills.append(amount)
    print("Electricity Bill: Rs.", round(amount, 2))

print("\nMonthly Bill Comparison")

for i in range(len(bills)):
    print("Month", i + 1, ":", round(bills[i], 2))

    if i > 0:
        previous = bills[i - 1]

        if previous > 0:
            increase = (bills[i] - previous) / previous * 100

            if increase > 30:
                print("Alert: Unusual bill increase!")
