""" Input - N times
    {Name : [score1, score2, score3]}
"""
students = {}
n = int(input('Insertions: '))
for i in range(n):
    entry = str(input('Entry: ')).split(' ')
    students.update({entry[0]: [float(entry[1]), float(entry[2]), float(entry[3])]})
# print(students)
# print('')

"""Query the user(search) and calculate the percentage
"""

# Percentage Calculation
query = input('Search: ')
summ = 0
if query in students:
    for i in students.get(query):
        summ += i
        # print(i)
    print("%.2f" % round(summ/len(students.get(query)), 2))
else:
    print('Not found.')