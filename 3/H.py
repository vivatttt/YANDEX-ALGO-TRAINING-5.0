with open('input.txt', 'r', encoding='utf-8') as inp:
    n = int(inp.readline())
    vector1 = dict()
    vector2 = dict()

    for _ in range(n):
        x1, y1, x2, y2 = map(int, inp.readline().split())
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        if x1 - x2 == 0 or y1 - y2 == 0:
            v = (abs(x2 - x1), abs(y2 - y1))
        else:
            v = (x2 - x1, y2 - y1)

        if v in vector1.keys():
            vector1[v].add((x1, y1, x2, y2))
        else:
            vector1[v] = {(x1, y1, x2, y2)}
    
    for _ in range(n):
        x1, y1, x2, y2 = map(int, inp.readline().split())
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        if x1 - x2 == 0 or y1 - y2 == 0:
            v = (abs(x2 - x1), abs(y2 - y1))
        else:
            v = (x2 - x1, y2 - y1)

        if v in vector2.keys():
            vector2[v].add((x1, y1, x2, y2))
        else:
            vector2[v] = {(x1, y1, x2, y2)}

    result = dict()

    for v in vector1.keys():
        if v in vector2.keys():
            d = set()
            for ax, ay, bx, by in vector1[v]:
                for cx, cy, ex, ey in vector2[v]:
                    
                    x1 = (ax + bx) / 2
                    y1 = (ay + by) / 2
                    x2 = (cx + ex) / 2
                    y2 = (cy + ey) / 2
                    dx = x2 - x1
                    dy = y2 - y1
                    
                    result[(dx, dy)] = result.get((dx, dy), 0) + 1
    
    maxx = 0
    for key in result.keys():
        if result[key] > maxx:
            maxx = result[key]     

print(n - maxx)