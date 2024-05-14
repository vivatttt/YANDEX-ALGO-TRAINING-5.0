with open('input.txt', 'r', encoding='utf-8') as inp:
    n = int(inp.readline())
    arr = list(map(int, inp.readline().split()))

    d = dict()

    for el in arr:
        d[el] = d.get(el, 0) + 1

    
    
    minn = float('inf')
    r = max(arr) 
    for i in range(1, r):
        cur = d.get(i, 0) + d.get(i + 1, 0)
        minn = min(minn, n - cur)
        
print(minn)