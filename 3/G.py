def points_of_square(x1, y1, x2, y2):
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    dx = x2 - x1
    dy = y2 - y1

    return [(x1 - dy, y1 + dx), (x2 - dy, y2 + dx), (x1 + dy, y1 - dx), (x2 + dy, y2 - dx)]

with open('input.txt', 'r', encoding='utf-8') as inp:
    n = int(inp.readline())
    arr = []
    for _ in range(n):
        arr.append(tuple(map(int, inp.readline().split())))

    if len(arr) == 1:
        x = arr[0]
        y = arr[1]
        print(3)
        print(x + 1, y)
        print(x, y + 1)
        print(x + 1, y + 1)
    else:
        dict_coords = dict()
        res = []
        for el in arr:
            dict_coords[el] = 1
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                x1, y1 = arr[i]
                x2, y2 = arr[j]

                p1, p2, p3, p4 = points_of_square(x1, y1, x2, y2)
                
                if p1 in dict_coords.keys() and p2 in dict_coords.keys():
                    res = []
                    break
                elif p3 in dict_coords.keys() and p4 in dict_coords.keys():
                    res = []
                    break
                elif p1 in dict_coords.keys():
                    res = [p2]
                elif p2 in dict_coords.keys():
                    res = [p1]
                elif p3 in dict_coords.keys():
                    res = [p4]
                elif p4 in dict_coords.keys():
                    res = [p3]
                elif not res:
                    res = [p1, p2]

            if not res:
                break

print(len(res))
for el in res:
    print(*el)