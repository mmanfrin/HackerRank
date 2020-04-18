def split_and_join(line):
    a = line.split(' ')
    b = '-'.join(a)
    return b


line = 'split and join'
print(split_and_join(line))