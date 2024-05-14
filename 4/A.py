def binsearch(arr, n, a, b):
    l, r = 0, n - 1
    left, right = 0, n - 1

    if arr[r] < a or arr[l] > b:
        return 0
    
    # ищем левую границу
    if arr[l] < a:
        while r - l > 1:
            m = (l + r) // 2
            if arr[m] < a:
                
                l = m
            else:
                r = m - 1
    
        if arr[r] >= a:
            left = l
        else:
            left = r
    else:
        left -= 1
    
    l, r = 0, n - 1

    if arr[r] > b:
        while r - l > 1:
            m = (l + r) // 2
            if arr[m] > b:
                r = m
            else:
                l = m + 1

        if arr[l] <= b:
            right = r
        else:
            right = l
    else:
        right += 1

    return right - left - 1


with open('input.txt', 'r', encoding='utf-8') as inp:
    n = int(inp.readline())
    arr = list(map(int, inp.readline().split()))
    arr.sort()
    k = int(inp.readline())
    res = []
    for _ in range(k):
        a, b = map(int, inp.readline().split())
        
        res.append(binsearch(arr, n, a, b))
print(*res)

