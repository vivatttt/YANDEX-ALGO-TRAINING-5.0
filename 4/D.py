def height(w, n, m, a, b, k):
    # функция, которая возвращает что длиннее - правый или левый столбец + длину максимального столбца
    hl = 0
    # левый столбец
    cur_st = a[0]

    for i in range(1, n):
        if cur_st + 1 + a[i] <= k:
            cur_st += 1 + a[i]
  
        else:
            hl += 1
            cur_st = a[i]
        
    hr = 0
    cur_st = b[0]
    for i in range(1, m):
        if cur_st + 1 + b[i] <= w - k:
            cur_st += 1 + b[i]
        else:
            hr += 1
            cur_st = b[i]

    hr += 1
    hl += 1     
    
    if hr > hl:
        return ['right', hr]
    elif hr < hl:
        return ['left', hl]
    return ['both', hl]
    


with open('input.txt', 'r', encoding='utf-8') as inp:
    w, n, m = map(int, inp.readline().split())
    a = list(map(int, inp.readline().split()))
    b = list(map(int, inp.readline().split()))

    l, r = max(a), w - max(b)
    min_h = float("inf")
    while r - l > 1:
        k = (r + l) // 2
        longer, h = height(w, n, m, a, b, k)
        if min_h == float("inf"):
            min_h = h
        else:
            min_h = min(min_h, h)

        if longer == 'right':
            r = k
        else:
            l = k
    min_h = min(min_h, height(w, n, m, a, b, r)[1])
    min_h = min(min_h, height(w, n, m, a, b, l)[1])

print(min_h)