class Student:
    def __init__(self, name , age, grade):
        self.name =name
        self.age =age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

st1 = Student('First', 18, 55)
st2 = Student('Second', 19, 66)
st3 = Student('Third', 91, 99)

course_a  = Course('Math', 2)
course_a.add_student(st1)
print(course_a)
print(course_a.students[0].name)


course_a.add_student(st2)
print(course_a.students[1].name)

print(course_a.add_student(st3))
print(course_a.get_average_grade())


