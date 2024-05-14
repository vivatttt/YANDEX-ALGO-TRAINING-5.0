def search(prefix, n, num, s):
    l, r = 0, n
    res = -1
    while r - l > 1:
        m = (l + r) // 2
        if m - l < 0:
            break
        f = prefix[m] - prefix[m - num]
        if f == s:
            res = m - num + 1
            break
        elif f > s:
            r = m
        else:
            l = m

    if res == -1:
        if r - num >= 0:
            if prefix[r] - prefix[r - num] == s:
                res = r - num + 1
        if l - num >= 0:
            if prefix[l] - prefix[l - num] == s:
                res = l - num + 1

            
    return res

with open('input.txt', 'r', encoding='utf-8') as inp:

    n, m = map(int, inp.readline().split())
    arr = list(map(int, inp.readline().split()))
    # создадим массив префиксных сумм
    prefix = [0]
    for i in range(n):
        prefix.append(prefix[i] + arr[i])

    res = []
    for _ in range(m):
        l, s = map(int, inp.readline().split())
        res.append(search(prefix, n, l, s))
print(*res)
               