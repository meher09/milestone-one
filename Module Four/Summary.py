students = ['Sony', 'Samrat', 'Rony', 'Mony', 'Jony']
#              0        1       2       3       4
#              -5       -4      -3      -2      -1
# print(students[0])
# print(students[-1])
# students.append('pony')
# students.insert(2,'Jahangir')
# students[1:3] = ['Aminul']
# students.remove('Rony')
# students.pop(1)
# print(students)
# s = '---'.join(students)
# students.sort(reverse=True)
# print(students)

# while True:
#     code block

number = [21,54,8,3,64,62,63,91,9,7,95,36]

i = 0
while i < len(number):
    if number[i] % 2 == 0:
        print(number[i], 'Even Number')
    i = i + 1