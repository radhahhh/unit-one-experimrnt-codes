n = int(input("Enter number of passengers: "))
distance = float(input("Enter distance in km: "))

print("1. Sleeper")
print("2. AC")
travel_class = int(input("Enter class: "))

total = 0

if n <= 0 or distance <= 0 or travel_class not in (1, 2):
    print("Invalid input")
else:
    if distance <= 100:
        base = distance * 1
    elif distance <= 500:
        base = 100 + (distance - 100) * 0.80
    else:
        base = 100 + 400 * 0.80 + (distance - 500) * 0.60

    if travel_class == 2:
        base = base * 2
        reservation = 60
    else:
        reservation = 30

    for i in range(n):
        name = input("Passenger name: ")
        age = int(input("Enter age: "))

        if age < 0:
            print("Invalid age")
            continue

        if age < 5:
            fare = 0
        elif age <= 11:
            fare = base * 0.50 + reservation
        elif age >= 60:
            fare = base * 0.60 + reservation
        else:
            fare = base + reservation

        total = total + fare
        print(name, "Fare: Rs.", round(fare, 2))

    print("Total Railway Fare: Rs.", round(total, 2))

    cancel = input("Cancel all tickets? yes/no: ")

    if cancel.lower() == "yes":
        penalty = total * 0.20
        refund = total - penalty

        print("Cancellation Penalty:", round(penalty, 2))
        print("Refund Amount:", round(refund, 2))
