from copy import deepcopy
def find_rectangle(arr, n, m, letter):
    # ищем левый верхний угол первого прямоугольника
    i0, j0 = -1, -1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == '#':
                i0 = i
                j0 = j
                break
        if i0 != -1:
            break

    if i0 == -1:
        return None
    
    # проходимся по столбцам, и считаем ширину нашего прямоугольника
    w = 0
    for j in range(j0, m):
        if arr[i0][j] == '#':
            arr[i0][j] = letter
            w += 1
        else:
            break
    
    # идем вниз и считаем высоту прямоугольника
    h = 1
  
    for i in range(i0 + 1, n):
        flag = 1
        for j in range(j0, j0 + w):
 
            if arr[i][j] == '.':
                flag = 0
                break
        if not flag:
            break
        
        for j in range(j0, j0 + w):
            arr[i][j] = letter

        h += 1
    return arr
def find_first_rectangle(arr, n, m):
    # ищем левый верхний угол первого прямоугольника
    i0, j0 = -1, -1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == '#':
                i0 = i
                j0 = j
                break
        if i0 != -1:
            break

    if i0 == -1:
        return None
    
    # проходимся по столбцам, и считаем ширину нашего прямоугольника
    w = 0
    for j in range(j0, m):
        if arr[i0][j] == '#':
            arr[i0][j] = 'a'
            w += 1
        else:
            break
    
    # идем вниз и считаем высоту прямоугольника
    h = 1
  
    for i in range(i0 + 1, n):
        flag = 1
        for j in range(j0, j0 + w):
 
            if arr[i][j] == '.':
                flag = 0
                break
        if not flag:
            break
        
        for j in range(j0, j0 + w):
            arr[i][j] = 'a'

        h += 1
    return arr

def find_second_rectangle(arr, n, m):
    # ищем левый верхний угол первого прямоугольника
    i0, j0 = -1, -1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == '#':
                i0 = i
                j0 = j
                break
        if i0 != -1:
            break

    if i0 == -1:
        return None
    
    # проходимся по столбцам, и считаем ширину нашего прямоугольника
    w = 0
    for j in range(j0, m):
        if arr[i0][j] == '#':
            arr[i0][j] = 'b'
            w += 1
        elif arr[i0][j] == 'a':
            arr[i0][j] = 'c'
            w += 1
        else:
            break
    
    # идем вниз и считаем высоту прямоугольника
    h = 1
  
    for i in range(i0 + 1, n):
        flag = 1
        for j in range(j0, j0 + w):
 
            if arr[i][j] == '.':
                flag = 0
                break
        if not flag:
            break
        
        for j in range(j0, j0 + w):
            if arr[i][j] == '#':
                arr[i][j] = 'b'
            else:
                arr[i][j] = 'c'
        h += 1
    return arr

def count(arr, n, m, letter):
    count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == letter:
                count += 1
    return count


with open('input.txt', 'r', encoding='utf-8') as inputfile:
    n, m = map(int, inputfile.readline().split())
    arr = []
    for _ in range(n):
        inp = inputfile.readline().strip()
        arr.append(list(inp))
    
    arr_copy = deepcopy(arr)
    arr = find_first_rectangle(arr, n, m)
    if not arr:
        res = 0
    else:
        if count(arr, n, m, '#') > 0:
            arr = find_second_rectangle(arr, n, m)
            if count(arr, n, m, '#') > 0:
                arr = find_rectangle(arr_copy, n, m, 'a')

                if not arr:
                    res = 0
                else:
                    if count(arr, n, m, '#') > 0:
                        arr = find_rectangle(arr, n, m, 'b')
                        if count(arr, n, m, '#') > 0:
                            res = 0
                        else:
                            res = 1
                    else:
                        if count(arr, n, m, 'a') == 1:
                            res = 0
                        else:
                            i0 = -1
                            j0 = -1
                            for i in range(n):
                                for j in range(m):
                                    if arr[i][j] == 'a':
                                        i0 = i
                                        j0 = j
                                        break
                                if i0 != -1:
                                    break
                            
                            w = 0
                            for j in range(j0, m):
                                if arr[i0][j] == 'a':
                                    w += 1
                                else:
                                    break
                            
                            if w == 1:
                                arr[i0][j0] = 'b'
                            else:
                                i = i0
                                while i < n:
                                    if arr[i][j0] == 'a':
                                        arr[i][j0] = 'b'
                                    else:
                                        break
                                    i += 1  
                            
                            res = 1
            elif count(arr, n, m, 'c') == 0:
                res = 1
            else:
                # прямоугольники пересекаются, их точки пересечения - c
                rows = []
                cols = []
                for i in range(n):
                    rows.append(''.join(arr[i]))
                for j in range(m):
                    s = ''
                    for i in range(n):
                        s += arr[i][j]
                    cols.append(s)
                    s = ''

                flag_row = 1
                flag_col = 1
                for row in rows:
                    if 'bc' in row and 'cb' in row:
                        flag_row = 0
                        break
                for col in cols:
                    if 'ac' in col and 'ca' in col:
                        flag_col = 0
                        break
                
                if not flag_row and not flag_col:
                    res = 0
                elif flag_row:
                    for i in range(n):
                        for j in range(m):
                            if arr[i][j] == 'c':
                                arr[i][j] = 'a'
                    res = 1
                else:
                    for i in range(n):
                        for j in range(m):
                            if arr[i][j] == 'c':
                                arr[i][j] = 'b'
                    res = 1

        else:
            if count(arr, n, m, 'a') == 1:
                res = 0
            else:
                i0 = -1
                j0 = -1
                for i in range(n):
                    for j in range(m):
                        if arr[i][j] == 'a':
                            i0 = i
                            j0 = j
                            break
                    if i0 != -1:
                        break
                
                w = 0
                for j in range(j0, m):
                    if arr[i0][j] == 'a':
                        w += 1
                    else:
                        break
                
                if w == 1:
                    arr[i0][j0] = 'b'
                else:
                    i = i0
                    while i < n:
                        if arr[i][j0] == 'a':
                            arr[i][j0] = 'b'
                        else:
                            break
                        i += 1  
                
                res = 1



with open('output.txt', 'w', encoding='utf-8') as outputfile:
    if not res:
        outputfile.write('NO')
 
    else:
        outputfile.write('YES\n')

        for i in range(n):
            s = ''.join(arr[i])
            s += '\n'
            outputfile.write(s)
 