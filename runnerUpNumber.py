# n = int(input())
arr = list(map(int, input().split()))
n = 5
# arr = [9, 1, 7, 8, 9, 5, 9, 7, 4]
# arr = [2, 3, 6, 6, 5,]
arr.sort()
ru = -101
maxi = -101

for i in range(len(arr)):
    if arr[i] > maxi:
        ru = maxi
        maxi = arr[i]
        
    # print(f'maxi={maxi} - ru={ru}')
print(ru)


# Alternative solution
z = max(arr)
while max(arr) == z:
    arr.remove(max(arr))

print(max(arr))