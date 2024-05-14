input()
arr = list(map(int, input().split()))

m = max(arr)
s = sum(arr)

res = 2 * m - s if 2 * m - s > 0 else s
print(res)