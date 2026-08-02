class Student:
    def __init__(self, name:str, marks:list[int]):
        self.name = name
        self.marks = marks

    def average(self)->float:
        return sum(self.marks) / len(self.marks)

    def grade(self)->str:
        avg = self.average()
        if avg >= 80:
            return "A"
        elif avg >= 65:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

    def display(self):
        avg = self.average()
        status = "pass" if avg >= 40 else "fail"
        print(f"{self.name} - average: {avg}, grade: {self.grade()}, {status}")


students_data = [
    ("Aarav", [78, 85, 60, 90, 72]),
    ("Sita", [45, 50, 38, 60, 55]),
    ("Bishal", [30, 25, 40, 35, 28]),
    ("Priya", [90, 88, 95, 92, 87]),
]

students = [Student(name, marks) for name, marks in students_data]

for s in students:
    s.display()