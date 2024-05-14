def solution(arr):
    res = []
    cur = [arr[0]]
    cur_min = arr[0]
    for i in range(1, len(arr)):

        if len(cur) + 1 <= min(cur_min, arr[i]):
            cur_min = min(cur_min, arr[i])
            cur.append(arr[i])
        else:
            res.append(len(cur))
            cur = [arr[i]]
            cur_min = arr[i]
    res.append(len(cur))
    return  res



t = int(input())
res = []
for _ in range(t):
    input()
    inp = list(map(int, input().split()))
    res.append(solution(inp))

for el in res:
    print(len(el))
    print(*el)

