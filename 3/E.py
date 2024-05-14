with open('input.txt', 'r', encoding='utf-8') as inp:
    inp.readline()
    a = list(map(int, inp.readline().split()))
    inp.readline()
    b = list(map(int, inp.readline().split()))
    inp.readline()
    c = list(map(int, inp.readline().split()))

    ab = set(a) & set(b)
    ac = set(a) & set(c)
    bc = set(b) & set(c)

    res = sorted(list(set(ab | ac | bc)))
    print(*res)