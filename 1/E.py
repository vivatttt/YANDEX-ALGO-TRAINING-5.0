import sys
sys.set_int_max_str_digits(10**6)
n, k, d = map(int, input().split())
flag = 1

if n % k != 0:
    n *= 10
    rem = n % k
    a = k - rem if rem != 0 else 0
    if a < 10:
        n += a
        print(n * 10 ** (d - 1))
    else:
        print(-1)
else:
    print(n * 10 ** d)