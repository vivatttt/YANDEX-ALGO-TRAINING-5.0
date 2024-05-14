def min_len(k):
    if k == 1:
        return 1
    l = k
    for i in range(2, k + 1):
        l += i * (k - i + 2)
    
    return l

with open('input.txt', 'r', encoding='utf-8') as inp:
    n = int(inp.readline())

    l = 1
    r = int(n ** 0.4) if n > 10 ** 10 else int(n ** 0.5)
    res = 1
    while r - l > 0:
        m = (r + l) // 2

        if min_len(m) <= n:
            res = max(res, m)
            l = m + 1
        else:

            r = m 
    
    if min_len(r) <= n:
        res = max(res, r)
if n == 0:
    print(n)
else:
    print(res)
