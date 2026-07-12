student_list = ["Alice", "Bob", "Charlie", "David", "Eva"]

attendance = {}

for i in range(2):
    print(f"attendance in {i} day")

    attendance[i] = {}
    for student in student_list:
            att = input(f"is {student} present or absent ")
            attendance[i][student] = att.lower()

print(attendance)