input()

arr = list(map(int, input().split()))
last = abs(arr[0]) % 2
operations = ''

for i in range(1, len(arr)):
    cur = abs(arr[i]) % 2
    if last == 1 and cur == 1:
        last *= cur
        operations += chr(120)
    else:
        last += cur
        operations += chr(43)
    last %= 2
    
print(operations)

