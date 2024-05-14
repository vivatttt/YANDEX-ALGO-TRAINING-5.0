l, x1, v1, x2, v2 = map(int, input().split())

if x1 == 0 and v1 <= 0:
    x1 = l
if x2 == 0 and v2 <= 0:
    x2 = l


if x1 == x2:
    print('YES')
    print(0)
elif v1 == 0 and v2 == 0:
    print('NO')
elif v1 == v2:
    m = (x1 + x2) / 2
    if v1 > 0:
        if m <= l / 2:
            s = l / 2 - m
        else:
            s = l - m
    else:
        if m >= l / 2:
            s = m - l / 2
        else:
            s = m

    t = abs(s / v1)
    print('YES')
    print(t)

elif v1 == -v2:
    
    v = v1 - v2

    if v > 0:
        if x1 >= x2:
            s = l - abs(x1 - x2)
        else:
            s = abs(x1 - x2)
            print(s)
    elif v < 0:
        if x1 >= x2:
            s = abs(x1 - x2)
        else:
            s = l - abs(x1 - x2)

    t = abs(s / v)
    print('YES')
    print(t)
   
else:
    # первая часть
    v = v1 - v2
    if v > 0:
        if x1 >= x2:
            s = l - abs(x1 - x2)
        else:
            s = abs(x1 - x2)
    elif v < 0:
        if x1 >= x2:
            s = abs(x1 - x2)
        else:
            s = l - abs(x1 - x2)

    t1 = abs(s / v)
    # вторая часть 
    v = v1 + v2
    x2_1 = l - x2
    if v > 0:
        if x1 >= x2_1:
            s = l - abs(x1 - x2_1)
        else:
            s = abs(x1 - x2_1)
    elif v < 0:
        if x1 >= x2_1:
            s = abs(x1 - x2_1)
        else:
            s = l - abs(x1 - x2_1)

    t2 = abs(s / v)
    print('YES')
    print(min(t1, t2))