plans = [
    ("Basic", 199, 300, 2, 28, 1, 20),
    ("Standard", 399, 600, 5, 28, 0.75, 15),
    ("Premium", 599, 1000, 10, 56, 0.50, 10)
]

minutes = int(input("Required call minutes: "))
data = float(input("Required data in GB: "))
days = int(input("Required validity in days: "))
budget = float(input("Enter budget: "))

best_plan = ""
minimum_cost = 0

if minutes < 0 or data < 0 or days <= 0 or budget < 0:
    print("Invalid input")
else:
    for plan in plans:
        name, price, free_minutes, free_data, validity, call_rate, data_rate = plan

        if validity >= days:
            extra_calls = max(0, minutes - free_minutes)
            extra_data = max(0, data - free_data)

            total = price + extra_calls * call_rate + extra_data * data_rate

            print(name, "Total Cost: Rs.", round(total, 2))

            if total <= budget:
                if best_plan == "" or total < minimum_cost:
                    best_plan = name
                    minimum_cost = total

    if best_plan == "":
        print("No plan available within budget")
    else:
        print("Best Plan:", best_plan)
        print("Minimum Cost: Rs.", round(minimum_cost, 2))
