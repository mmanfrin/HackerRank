students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], 
     ['Akriti', 41], ['Harsh', 39]]

# Input List Loop
# students = []
# for _ in range(int(input('N: '))):
#     name = input('Name: ')
#     score = float(input('Score: '))
#     students.append([name, score])    
print(students)

# get second lowest grade
lowest = 100000
lowest2 = 100000
for i in range(len(students)):
    # print(students[i][1])
    if students[i][1] < lowest:
        lowest2 = lowest
        lowest = students[i][1]
# print(lowest, lowest2)

# Get names form 2nd lower grades
names = []
for i in range(len(students)):
    if lowest2 in students[i]:
        names.append(students[i][0])
names = sorted(names)

# print(names)
for i in range(len(names)):
    print(names[i])