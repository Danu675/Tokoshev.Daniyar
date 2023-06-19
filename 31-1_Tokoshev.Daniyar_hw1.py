class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Full Name: {self.fullname}")
        print(f"Age: {self.age}")
        print(f"Marital Status: {'Married' if self.is_married else 'Single'}")


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def calculate_average_mark(self):
        total_marks = sum(self.marks.values())
        average_mark = total_marks / len(self.marks)
        return average_mark


class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = salary

    def calculate_salary(self):
        bonus_percentage = max(0, self.experience - 3) * 0.05
        total_salary = self.salary + (self.salary * bonus_percentage)
        return total_salary


def create_students():
    student1 = Student("Ivan", 16, False, {"Math": 85, "Science": 92, "History": 78})
    student2 = Student("Danya", 17, False, {"Math": 90, "Science": 88, "History": 95})
    student3 = Student("Bob ", 16, False, {"Math": 76, "Science": 82, "History": 80})
    students = [student1, student2, student3]
    return students


teacher = Teacher("Alexandr", 35, True, 8, 5000)
teacher.introduce_myself()
print(f"Salary: {teacher.calculate_salary()}")
students_list = create_students()
for student in students_list:
    student.introduce_myself()
    print("Marks:")
    for subject, mark in student.marks.items():
        print(f"{subject}: {mark}")
    average_mark = student.calculate_average_mark()
    print(f"Average Mark: {average_mark}")
