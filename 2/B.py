from collections import deque
n, k = map(int, input().split())
arr = list(map(int, input().split()))

delta = 0
dq = deque()
dq.append(arr[0])

k = min(n, k + 1)

for i in range(1, k):
    
    while dq:
        if dq[-1] > arr[i]:
            dq.pop()
        else:
            break 
    dq.append(arr[i])

    delta = max(delta, arr[i] - dq[0])

l, r = 0, k

while r < n:

    if arr[l] == dq[0]:
        dq.popleft()

    while dq:
        if dq[-1] > arr[r]:
            dq.pop()
        else:
            break 
    dq.append(arr[r])

    delta = max(delta, arr[r] - dq[0])
    r += 1
    l += 1

print(delta)