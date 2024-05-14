def isvalid(arr, i, m, maxx, vert_prefix):
    j = maxx - (arr[i][0] + m)  + 1
    if j <= 0:
        return True
    if m >= vert_prefix[j]:
        return True
    return False
 

with open('input.txt', 'r', encoding='utf-8') as inp:
    n = int(inp.readline())
    arr = []
    maxx = 0
    max_count = 0
    for i in range(n):
        v, p = map(int, inp.readline().split())
        if v > maxx:
            maxx = v
            max_count = 1
        elif v == maxx:
            max_count += 1
        arr.append([v, p, i + 1])

    arr.sort(key=lambda el: el[0], reverse=True)

    if n == 1:
        print(arr[0][1])
        print(1)
        print(arr[0][i])
    else:
        vert_prefix = [0]
        # заполняем массив префиксных сумм для вертикальных столбиков
        h = maxx
        i = 1
        cur = 1
        while h > 0 and i < n:
            if h == arr[i][0]:
                cur += 1
                i += 1
            else:
                vert_prefix.append(cur + vert_prefix[-1])
                h -= 1
        vert_prefix.append(cur)
        
        res = None
        for i in range(n):
            v, p = arr[i][0], arr[i][1]
            if p != -1:
                if v != maxx:
                    l, r = 0, maxx
                    while r - l > 0:
                        m = (l + r) // 2
                        
                        if isvalid(arr, i, m, maxx, vert_prefix):
                            if not res:
                                res = [m + p, i]
                            else:
                                if res[0] > m + p:
                                    res = [m + p, i]
                            r = m
                        else:
                            l = m + 1
                else:
                    if max_count > 1:
                        p += 1

                    if not res:
                        res = [p, i]
                    else:
                        if res[0] > p:
                            res = [p, i]

        k = res[1]
        m = res[0] - arr[k][1]

        print(res[0])
        print(arr[k][2])
        if arr[k][0] == maxx and max_count > 1:
            arr[k][0] += 1
            for i in range(n):
                if i != k and arr[i][0] == maxx:
                    arr[i][0] -= 1
                    break
            # print(res, maxx, arr[res[1]][0])
            # # ищем максимум, к которому будем прибавлять и из которого будем вычитать
            # r = 0
            # for i in range(n):
            #     if arr[i][1] != -1:
            #         r = i
            #         break
            # if r == 0:
            #     arr[0][0] += 1
            #     arr[1][0] -= 1
            # else:
            #     arr[r][0] += 1
            #     arr[0][0] -= 1

        else:
            
            d = m - vert_prefix[maxx - (arr[k][0] + m)  + 1]

            for i in range(k):
                f = 1
                if d > 0:
                    f = 2
                    d -= 1
                arr[i][0] = min(arr[k][0] + m - f, arr[i][0])

            arr[k][0] = arr[k][0] + m

        arr.sort(key=lambda el: el[2])

        for el in arr:
            print(el[0], end=' ')