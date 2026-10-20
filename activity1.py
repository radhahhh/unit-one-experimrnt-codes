students = []
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = []

    for j in range(3):
        mark = int(input("Enter subject mark: "))
        marks.append(mark)

    attendance = float(input("Attendance percentage: "))
    income = float(input("Annual family income: "))

    total = sum(marks)
    aggregate = total / 3

    if (min(marks) >= 60 and aggregate >= 75
        and attendance >= 80 and income <= 300000):
        students.append((name, aggregate,
                         attendance, income))
        print(name, "is Eligible")
    else:
        print(name, "is Not Eligible")

# Ranking eligible students
for i in range(len(students)):
    for j in range(i + 1, len(students)):
        a = students[i]
        b = students[j]

        if ((b[1] > a[1]) or
            (b[1] == a[1] and b[2] > a[2]) or
            (b[1] == a[1] and b[2] == a[2]
             and b[3] < a[3]) or
            (b[1] == a[1] and b[2] == a[2]
             and b[3] == a[3] and b[0] < a[0])):
            students[i], students[j] = students[j], students[i]

print("\nScholarship Ranking")

for i in range(len(students)):
    print(i + 1, students[i][0],
          "Aggregate:", students[i][1])
