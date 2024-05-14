import math

with open('input.txt', 'r', encoding='utf-8') as inp:
    k = int(inp.readline())
    n = math.ceil((2 * k + 0.25) ** 0.5 - 0.5)

    if n * (n + 1) // 2 < k:
        n += 1

    pre_sum = (n * (n - 1)) // 2
    k -= pre_sum
   
    res = f'{k}/{n - k + 1}' if n % 2 == 1 else f'{n - k + 1}/{k}'

print(res)

