students = [['sona', -50], ['mona', -50], ['mini', -50], ['rita', 51]]
students.sort(key=lambda student: student[1])
while students[0][1] == students[1][1]:
    students.pop(0)
students.pop(0)
print(students)
names = [x for x in students if x[1] == students[0][1]]

names.sort(key=lambda names: names[0])
for name in names:
    print(name[0])



