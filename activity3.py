name = input("Enter patient name: ")
age = int(input("Enter age: "))
income = float(input("Enter annual income: "))

consultation = float(input("Consultation charges: "))
diagnostic = float(input("Diagnostic charges: "))
treatment = float(input("Treatment charges: "))

if (age < 0 or income < 0 or consultation < 0
    or diagnostic < 0 or treatment < 0):
    print("Invalid input")
else:
    total = consultation + diagnostic + treatment

    if age >= 60:
        discount = 0.15
    elif income < 200000:
        discount = 0.10
    else:
        discount = 0

    concession = total * discount
    net_bill = total - concession

    print("\nHOSPITAL BILL")
    print("Patient:", name)
    print("Total Charges:", total)
    print("Concession:", concession)
    print("Net Bill:", net_bill)

    paid = float(input("Enter amount paid: "))

    if paid < 0 or paid > net_bill:
        print("Invalid payment")
    elif paid == net_bill:
        print("Classification: Fully Paid")
    elif paid == 0:
        print("Classification: Unpaid")
    else:
        print("Classification: Partially Paid")
        print("Balance:", net_bill - paid)
