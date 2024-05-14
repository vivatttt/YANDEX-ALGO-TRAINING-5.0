with open('input.txt', 'r', encoding='utf-8') as inpfile:
    n = int(inpfile.readline())
    sett = set()
    for _ in range(n):
        inpfile.readline()
        if not sett:
            sett = set(inpfile.readline().split())
        else:
        
            cur = set(inpfile.readline().split())
        
            sett &= cur
res = sorted(list(sett))
print(len(res))
print(*res)

