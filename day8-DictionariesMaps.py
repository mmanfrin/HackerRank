phonebook = {}
# phonebook = {'sam' : 123, 'tom' : 456, 'harry' : 789}
N = input('N: ')
for i in range(int(N)):
    entry = str(input('Entry: ')).split(" ")

    name = entry[0]
    number = int(entry[1])
    phonebook[name] = number

# Input List Loop
# for i in range(int(input('N: '))):
#     name = input('Name: ')
#     number = input('Number: ')
#     phonebook.update({name: number})
# #     # phonebook[name] = number
# # print(phonebook)

# Queries
for i in range(int(N)):
    query = input('Search: ')
    if query in phonebook:
        print(str(query) + ' = ' + str(phonebook.get(query)))
    else:
        print('Not found')

# query = 'sam'
# print(str(query) + '=' + str(phonebook.get(query)))