expenses = []

budget = float(input("Enter travel budget in INR: "))
n = int(input("Enter number of expenses: "))

total = 0
largest = 0
largest_category = ""

if budget < 0 or n <= 0:
    print("Invalid budget or expense count")
else:
    for i in range(n):
        category = input("Expense category: ")
        currency = input("Currency name: ")
        amount = float(input("Amount: "))
        rate = float(input("Exchange rate to INR: "))

        if amount < 0 or rate <= 0:
            print("Invalid amount or exchange rate")
            continue

        converted = amount * rate
        fee = converted * 0.02
        final_amount = converted + fee

        expenses.append((category, currency, final_amount))

        total = total + final_amount

        if final_amount > largest:
            largest = final_amount
            largest_category = category

    print("\nTRAVEL EXPENSE REPORT")

    for item in expenses:
        print(item[0], item[1], "Rs.", round(item[2], 2))

    print("Total Expenses: Rs.", round(total, 2))
    print("Budget: Rs.", budget)

    if total <= budget:
        print("Within Budget")
        print("Remaining Balance:", round(budget - total, 2))
    else:
        print("Budget Exceeded")
        print("Extra Amount:", round(total - budget, 2))

    print("Largest Expense Category:", largest_category)
