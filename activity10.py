event = input("Enter event name: ")

venue = float(input("Venue cost: "))
equipment = float(input("Equipment cost: "))
catering = float(input("Catering cost per participant: "))
transport = float(input("Total transport cost: "))
certificate = float(input("Certificate cost per participant: "))

participants = int(input("Expected participants: "))
registration_fee = float(input("Registration fee per participant: "))
sponsorship = float(input("Sponsorship amount: "))

if (venue < 0 or equipment < 0 or catering < 0
    or transport < 0 or certificate < 0
    or participants < 0 or registration_fee < 0
    or sponsorship < 0):
    print("Invalid input")
else:
    fixed_cost = venue + equipment + transport
    variable_cost = catering + certificate

    total_cost = fixed_cost + participants * variable_cost

    contribution = participants * registration_fee

    total_income = contribution + sponsorship

    balance = total_income - total_cost

    print("\nCAMPUS EVENT FINANCIAL REPORT")
    print("Event:", event)
    print("Total Event Cost: Rs.", round(total_cost, 2))
    print("Participant Contribution: Rs.", round(contribution, 2))
    print("Sponsorship: Rs.", sponsorship)
    print("Total Income: Rs.", round(total_income, 2))

    if balance >= 0:
        print("Event is Financially Successful")
        print("Surplus: Rs.", round(balance, 2))
    else:
        print("Sponsorship Shortfall: Rs.", round(-balance, 2))

    amount_needed = fixed_cost - sponsorship
    margin = registration_fee - variable_cost

    if amount_needed <= 0:
        minimum = 0
        print("Minimum Registrations:", minimum)
    elif margin <= 0:
        print("Break-even is not possible with current fees")
    else:
        minimum = 0

        while minimum * margin < amount_needed:
            minimum = minimum + 1

        print("Minimum Registrations to Break Even:", minimum)
