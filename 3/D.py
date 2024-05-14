with open('input.txt', 'r', encoding='utf-8') as inp:
    n, k = map(int, inp.readline().split())
    arr = list(map(int, inp.readline().split()))

    d = dict()
    flag = 0
    k = min(n, k)
    if n == k:
        print('YES' if len(set(arr)) != len(arr) else 'NO')
    else:
        for i in range(k + 1):
            d[arr[i]] = d.get(arr[i], 0) + 1
            if d[arr[i]] > 1:
                flag = 1
                break
        
        if flag:
            print('YES')
        else:
            l = 0
            r = k + 1
            while r < n:
                d[arr[l]] -= 1
                d[arr[r]] = d.get(arr[r], 0) + 1
                if d[arr[r]] > 1:
                    flag = 1
                    break
                r += 1
                l += 1
            print('YES' if flag else 'NO')