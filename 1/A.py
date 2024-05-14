v, d_v = map(int, input().split())
m, d_m = map(int, input().split())

m1, m2 = m - d_m, m + d_m
v1, v2 = v - d_v, v + d_v

if v2 > m2:
    v2, m2 = m2, v2
    v1, m1 = m1, v1



delta = 0
if v2 - m1 >= 0:
    delta = v2 - max(m1, v1) + 1

res = v2 - v1 + m2 - m1 + 2 - delta
print(res)
