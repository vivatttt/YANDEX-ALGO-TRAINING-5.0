def location(arr_max):
    x = dict()
    y = dict()

    for el in arr_max:
        if el[1] in x:
            x[el[1]] += 1
        else:
            x[el[1]] = 1
        if el[0] in y:
            y[el[0]] += 1
        else:
            y[el[0]] = 1
 
    count_x = 0
    count_y = 0
    i = 0
    j = 0
   
    for l in x.keys():
        if x[l] > count_x:
            count_x = x[l]
            j = l
    for l in y.keys():
        if y[l] > count_y:
            count_y = y[l]
            i = l

    if count_x + count_y == len(arr_max):
        return ['cross', i, j]
    elif sum(y.values()) == count_y:
        return ['v-line', i]
    elif sum(x.values()) == count_x:
        return ['h-line', j]
    
    return None
        

def find_max(arr,  n, m, exc1=None, exc2=None):
    # exc[0] - 0 - столбец, 1 - строка, exc[1] - номер
    maxx = 0
    for i in range(n):
        if exc1:
            if exc1[0] == 1 and exc1[1] == i:
                continue
        if exc2:
            if exc2[0] == 1 and exc2[1] == i:
                continue
        for j in range(m):
            if exc1:
                if exc1[0] == 0 and exc1[1] == j:
                    continue
            if exc2:
                if exc2[0] == 0 and exc2[1] == j:
                    continue
            maxx = max(maxx, arr[i][j])
    return maxx

def vertical(arr, n, m, j_closed):

    arr_remained_max = [(0, 0)]
    flag = 1
    for i in range(n):
        for j in range(m):
            if j == j_closed:
                continue

            if arr[arr_remained_max[0][0]][arr_remained_max[0][1]] < arr[i][j] or flag:
                arr_remained_max = [(i, j)]
                flag = 0
            elif arr[arr_remained_max[0][0]][arr_remained_max[0][1]] == arr[i][j]:
                arr_remained_max.append((i, j))

    if len(arr_remained_max) > n:
        res = [arr[arr_remained_max[0][0]][arr_remained_max[0][1]], 1, j_closed]
    elif location(arr_remained_max) != None and len(arr_remained_max) >= 2:
        flag = location(arr_remained_max)
        if flag[0] == 'v-line':
            res = [find_max(arr, n, m, [0, j_closed], [1, flag[1]]), flag[1], j_closed]
        else:
            res = [10**9, 0, j_closed]
    elif len(arr_remained_max) == 1:
        i_remained_closed = arr_remained_max[0][0]
        res = [find_max(arr, n, m, [0, j_closed], [1, i_remained_closed]), i_remained_closed, j_closed]
    else:
        res = [10**9, 0, 0]
    return res

def horizontal(arr, n, m, i_closed):
    arr_remained_max = [(0, 0)]
    flag = 1
    for i in range(n):
        if i == i_closed:
            continue
        for j in range(m):      
            if arr[arr_remained_max[0][0]][arr_remained_max[0][1]] < arr[i][j] or flag:
                arr_remained_max = [(i, j)]
                flag = 0
            elif arr[arr_remained_max[0][0]][arr_remained_max[0][1]] == arr[i][j]:
                arr_remained_max.append((i, j))
            

    if len(arr_remained_max) > m:
        res = [arr[arr_remained_max[0][0]][arr_remained_max[0][1]], i_closed, 1]
    elif location(arr_remained_max) != None and len(arr_remained_max) >= 2:
      
        flag = location(arr_remained_max)
        if flag[0] == 'h-line':
            res = [find_max(arr, n, m, [1, i_closed], [0, flag[1]]), i_closed, flag[1]]
        else:
            res = [10**9, i_closed, 0]
    elif len(arr_remained_max) == 1:
        
        j_remained_closed = arr_remained_max[0][1]
        
        res = [find_max(arr, n, m, [1, i_closed], [0, j_remained_closed]), i_closed, j_remained_closed]
    else:
        
        res = [10**9, 0, 0]
    return res

with open('input.txt', 'r') as input:
    n, m = map(int, input.readline().split())

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input.readline().split())))


    arr_max = [(0, 0)]

    for i in range(n):
        for j in range(m):
            if arr[arr_max[0][0]][arr_max[0][1]] < arr[i][j]:
                arr_max = [(i, j)]
            elif arr[arr_max[0][0]][arr_max[0][1]] == arr[i][j]:
                arr_max.append((i, j))

   
    if len(arr_max) > n + m:
        res = [10**9, 0, 0]

    elif (len(arr_max) > 2 and location(arr_max) != None):

        flag = location(arr_max)

        if flag[0] == 'cross':
            res = [0, flag[1], flag[2]]
        elif flag[0] == 'h-line':
            res = vertical(arr, n, m, flag[1])
  
        else:
            res = horizontal(arr, n, m, flag[1])
            

    elif len(arr_max) <= 2:
        res = [10 ** 9 + 1, 0, 0]
        for (i_closed, j_closed) in arr_max:
            
            # закрываем вертикаль
            # ищем все вторые максимумы с закрытой вертикалью
            h = horizontal(arr, n, m, i_closed)
            if h[0] < res[0]:
                res = h
            # закрываем горизонталь
            # ищем все вторые максимумы с закрытой горизонталью
            v = vertical(arr, n, m, j_closed)
            if v[0] < res[0]:
                res = v
        
    else:
        res = [10**9, 0, 0]


print(res[1] + 1, res[2] + 1)