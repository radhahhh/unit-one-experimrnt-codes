name = input("Employee name: ")
basic = float(input("Basic salary: "))
hours = float(input("Overtime hours: "))
incentive = float(input("Incentive amount: "))

if basic < 0 or hours < 0 or incentive < 0:
    print("Invalid salary details")
else:
    hra = basic * 0.20
    da = basic * 0.10
    overtime = hours * 200

    gross = basic + hra + da + overtime + incentive

    pf = basic * 0.12

    if gross <= 30000:
        tax = 0
    elif gross <= 60000:
        tax = (gross - 30000) * 0.05
    else:
        tax = 30000 * 0.05 + (gross - 60000) * 0.10

    deductions = pf + tax
    net_salary = gross - deductions

    print("\n------ SALARY STATEMENT ------")
    print("Employee:", name)
    print("Basic Salary: Rs.", basic)
    print("HRA: Rs.", hra)
    print("DA: Rs.", da)
    print("Overtime: Rs.", overtime)
    print("Incentive: Rs.", incentive)
    print("Gross Salary: Rs.", round(gross, 2))
    print("PF Deduction: Rs.", round(pf, 2))
    print("Tax: Rs.", round(tax, 2))
    print("Total Deductions: Rs.", round(deductions, 2))
    print("Net Salary: Rs.", round(net_salary, 2))
