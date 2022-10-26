class Student:

    def __init__(self, name, age, id):
        self.avg_grade = None
        if not name:
            raise ValueError('Missing name')
        self.name = name
        self.age = age
        self.id = id
        self.subjects = {}

    def add_subject(self, subject, grade):
        self.subjects[str(subject)] = int(grade)

    def remove_subject(self, subject):
        del self.subjects[str(subject)]

    def get_subjects(self):
        return self.subjects

    def get_grade(self):
        new_output = list(self.subjects.values())
        print('All students grades are:', new_output)

    def get_avggrade(self):
        average_grade = sum(self.subjects.values()) / len(self.subjects)
        self.avg_grade = average_grade
        return average_grade


class CFGStudent(Student):

    def __init__(self, name, age, id, specialization):
        super().__init__(name, age, id)
        self.specialization = specialization


student_1 = Student('Fola', 20, 1)
student_2 = Student('Jack', 19, 2)

student_3 = CFGStudent('Nada', 21, 3, 'data-science')

Student.add_subject(student_1, 'maths', 80)
Student.add_subject(student_1, 'english', 75)
Student.get_avggrade(student_1)
Student.get_grade(student_1)
Student.get_subjects(student_1)
print(student_1.subjects)
print(student_1.avg_grade)
print(student_3.specialization)
