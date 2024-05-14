def find_best_row(arr):
    count = dict()
    res = []
    for _, j in arr:
        count[j] = count.get(j, 0) + 1
    
    maxx = max(count.values())
 
    for j in count.keys():
        if count[j] == maxx:
            res.append(j)
    return res

def print_field(arr, n):
    field = [['0'] * n for _ in range(n)]

    for (i, j) in arr:
        field[i][j] = 1
    
    for i in range(n):
        print(*field[i])

def are_spare_lines(lines, n):
    flag = 0
    for i in range(n):
        if not lines[i]:
            flag = 1
            break
    return flag

def to_one_in_line(arr, n):
    lines = dict()

    for i in range(n):
        lines[i] = []
    for (i, j) in arr:
        lines[i].append(j)
    count = 0
    i = 0
    
    while are_spare_lines(lines, n):
        for i in range(n):
            if not lines[i]:
                break
             
        # нашли пустую строку
        # ищем ближайшую строку, в которой можно взять 1 элемент (те ее длина >= 2)
        up = -1
        for up in range(i - 1, -1 , -1):
            if len(lines[up]) >= 2:
                break
            else:
                up = -1
        down = -1
        for down in range(i + 1, n):
            
            if len(lines[down]) >= 2:
                break
            else:
                down = -1

        if up != -1:       
            count += (i - up)
            lines[i] = [lines[up][0]]
            del lines[up][0]
        else:
            count += (down - i)
            lines[i] = [lines[down][0]]
            del lines[down][0]
    arr = []
    for i in lines.keys():
        arr.append((i, lines[i][0]))

    return [arr, count]




with open('input.txt', 'r', encoding='utf-8') as inputfile:
    n = int(inputfile.readline())
    arr = []
    for _ in range(n):
        i, j = map(int, inputfile.readline().split())
        arr.append((i - 1, j -1))
    
    arr, count = to_one_in_line(arr, n)
    rows = find_best_row(arr)
    minn = float("inf")
    
    for row in range(n):
        count_rows = 0
        for (_, j) in arr:
            count_rows += (abs(j - row))
        minn = min(minn, count_rows)

print(count + minn)
