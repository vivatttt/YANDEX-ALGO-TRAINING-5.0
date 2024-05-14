n = int(input())
s = 0

for _ in range(n):
    a = int(input())
    
    s += a // 4
    a %= 4
    
    if a in (2, 3):
        s += 2
    elif a == 1:
        s += 1
    
print(s)