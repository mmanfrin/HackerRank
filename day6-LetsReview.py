"""Divide words based on its letter index(even or odd)
"""
# n = list(map(str, input().split()))
n = int(input('Number of entries: '))
# n = 2
words = []
l1 = []
l2 = []

for i in range(0,n):
    words.append(input('Input: '))
# words.insert(0, 'Hacker')
# words.insert(1, 'Rank')
# print(words)

for i in range(n):
    for j in range(len(words[i])):
        # print(j)
        if j % 2 == 0:
            l1.append(words[i][j])
        else:
            l2.append(words[i][j])
    print(''.join(l1), end=' ')
    print(''.join(l2))
            
    l1.clear()
    l2.clear()