with open('input.txt', 'r', encoding='utf-8') as inputfile:
    n = int(inputfile.readline())
    arr = list(map(int, inputfile.readline().split()))
    a, b, k = map(int, inputfile.readline().split())

if b <= k:
    res = arr[0]
elif  (b - a) // (n * k) >= 1:
    res = max(arr)
else:
    n1 = a // k
    n2 = b // k
    
    n1 %= n
    n2 %= n

    n1 = n1 - 1 if a % k == 0 else n1
    n2 = n2 - 1 if b % k == 0 else n2
    
    if n1 < 0:
        n1 += n
    if n2 < 0:
        n2 += n

    if n2 < n1:
        arr *= 2
        n2 += n
        res = max(max(arr[n1:n2 + 1]), max(arr[2 * n - n2: 2 * n - n1 + 1]))
    else:
        res = max(max(arr[n1:n2 + 1]), max(arr[n - n2: n - n1 + 1]))
print(res)