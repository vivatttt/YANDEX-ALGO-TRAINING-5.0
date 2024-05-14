from collections import deque

def is_valid(set_x, arr_x, min_right_arr, max_right_arr, k):
    x_to_del = deque()

    p_max = 0
    p_min = 0
    n_max = len(max_right_arr) - 1
    n_min = len(min_right_arr) - 1

    for i, el in enumerate(arr_x):
        if el > k:
            break
        else:
            x_to_del.append(el)

    for j in range(i):
        min_y, max_y = set_x[arr_x[j]]

        if p_min <= n_min:
            if min_right_arr[p_min] == min_y:
                p_min += 1
        if p_max <= n_max:
            if max_right_arr[p_max] == max_y:
                p_max += 1
    
    min_left_y = None
    max_left_y = None

    if p_min <= n_min and p_max <= n_max:
        if max_right_arr[p_max] - min_right_arr[p_min] < k:
            return True
    
    l, r = 1, k 

    while i < len(arr_x):
        
        new_r = arr_x[i]
        new_l = new_r - k + 1
        
        if min_left_y != None and max_left_y != None:
            if set_x[arr_x[i]][1] > max_left_y or set_x[arr_x[i]][0] < min_left_y:
                x_to_del.append(arr_x[i])
        else:
            x_to_del.append(arr_x[i])

        while x_to_del:
            if x_to_del[0] < new_l:
                x = x_to_del[0]
                x_to_del.popleft()

                if min_left_y == None:
                    min_left_y = set_x[x][0]
                else:
                    min_left_y = min(set_x[x][0], min_left_y)

                if max_left_y == None:
                    max_left_y = set_x[x][1]
                else:
                    max_left_y = max(set_x[x][1], max_left_y)
            else:
                break

        if p_min <= n_min:
            if min_right_arr[p_min] == set_x[arr_x[i]][0]:
                p_min += 1
        if p_max <= n_max:
            if max_right_arr[p_max] == set_x[arr_x[i]][1]:
                p_max += 1

        if p_min <= n_min and min_left_y:
            if min_right_arr[p_min] >= min_left_y:
                p_min = n_min + 1
        if p_max <= n_max and max_left_y:
            if max_right_arr[p_max] <= max_left_y:
                p_max = n_max + 1

        cur_min = None
        cur_max = None

        if p_min <= n_min and min_left_y != None:
            cur_min = min(min_right_arr[p_min ], min_left_y)
        elif p_min <= n_min:
            cur_min = min_right_arr[p_min]
        else:
            cur_min = min_left_y
        
        if p_max <= n_max and max_left_y != None:
            cur_max = max(max_right_arr[p_max], max_left_y)
        elif p_max <= n_max:
            cur_max = max_right_arr[p_max]
        else:
            cur_max = max_left_y
       
        if cur_max != None and cur_min != None:
            if cur_max - cur_min < k:
                return True
            
        if min_left_y != None and max_left_y != None:
            if max_left_y - min_left_y >= k:
                return False
        
        if not p_max <= n_max and not p_min <= n_min:
            if min_left_y != None and max_left_y != None:
                if max_left_y - min_left_y >= k:
                    return False
                else:
                    return True
            else:
                return False

        l, r = new_l, new_r
        i += 1

    return False


with open('input.txt', 'r', encoding='utf-8') as inp:
    w, h, n = map(int, inp.readline().split())
    arr = []
    for _ in range(n):
        arr.append(tuple(map(int, inp.readline().split())))
    arr = sorted(arr, key=lambda el: el[0])   
    set_x = dict()
    for x, y in arr:
        if x in set_x:
            set_x[x] = (min(set_x[x][0], y), max(set_x[x][1], y))
        else: 
            set_x[x] = (y, y)
    arr_x = list(set_x.keys())

    min_right_arr = []
    max_right_arr = []

    for j in range(len(arr_x)):
        
        min_y, max_y = set_x[arr_x[j]]
        while min_right_arr:
            if min_right_arr[-1] > min_y:
                min_right_arr.pop()
            else:
                break
        min_right_arr.append(min_y)
            
        while max_right_arr:        
            if max_right_arr[-1] < max_y:
                max_right_arr.pop()
            else:
                break
        max_right_arr.append(max_y)


    l, r = 1, min(w, h) + 1
    res = min(w, h)

    while r - l > 0:
        m = (l + r) // 2
        if is_valid(set_x, arr_x, min_right_arr, max_right_arr, m):
            res = m
            r = m 
        else:
            l = m + 1

print(res)       