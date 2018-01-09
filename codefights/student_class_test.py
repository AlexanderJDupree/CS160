class students:

    num_of_students = 0
    tuition_aid = 0.75
    tuition = 5000
    school = []

    def __init__(self, first, last, major):
        self.first = first
        self.last = last
        self.email = first + '.' + last + ".college.edu"
        self.major = major
        self.tuition = students.tuition
        self.school.append(self)
        students.num_of_students += 1

    def description(self):
        return "{} {} is studying {} and can be reached via email at {}."\
            .format(self.first, self.last, self.major, self.email)

    def apply_fin_aid(self):
        self.tuition = self.tuition * self.tuition_aid

    @classmethod
    def from_string(cls, stdnt_string):
        first, last, major = stdnt_string.split('-')
        return cls(first, last, major)


class teachers(students):

    num_teachers = 0
    teachers = []

    def __init__(self, first, last, department, pay):
        super().__init__(first, last, department)
        self.pay = pay
        teachers.num_teachers += 1
        self.teachers.append(self)


def main():
    student_1 = students("Alex", "DuPree", "Computer Science")
    student_2 = students("Addison", "Grace", "Biology")
    student_3 = students("Thor", "Cassius", "Nursing")

    teacher_1 = teachers("test", "Teacher", "math", 50000)

    stdnt_4_string = "John-Doe-Physics"
    stdnt_5_string = "Jane-Doe-Criminal_Justice"

    print(set(students.school).union(teachers.teachers))


main()
# if __name__ == '__main__':
# main()
