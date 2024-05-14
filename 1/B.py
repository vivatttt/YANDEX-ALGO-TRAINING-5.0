m1_t1, m1_t2 = map(int, input().split(':'))
m2_t1, m2_t2 = map(int, input().split(':'))
flag = int(input())

delta = m1_t2 + m2_t2 - (m1_t1 + m2_t1)
m2_t1 += delta if delta > 0 else 0

if ((flag == 1 and m2_t1 <= m1_t2) or (flag == 2 and m1_t1 <= m2_t2)) and delta >= 0: 
    delta += 1

print(delta if delta > 0 else 0)