n = int(input())
positive = []
negative = []
h = 0
for i in range(1, n + 1):
    a, b = map(int, input().split())

    if a - b >= 0:
        positive.append([a, b, i])
        h += (a - b)
    else:
        negative.append([a, b, i])

if positive:
    d = positive[0]
    for el in positive:
        if el[1] > d[1]:
            d = el

    h += d[1]

if negative and positive:
    maxx= negative[0]

    for el in negative:
        if el[0] > maxx[0]:
            maxx = el
    
    h = max(h, h - d[1] + maxx[0])
elif negative:
	maxx = negative[0]
	for el in negative:
		if el[0] > maxx[0]:
			maxx = el
	h = maxx[0]

res = []

for el in positive:
    if el[2] != d[2]:
        res.append(el[2])

if positive:
    res.append(d[2])

if negative:
    res.append(maxx[2])

for el in negative:
    if el[2] != maxx[2]:
        res.append(el[2])

print(str(h))
for el in res:
    print(str(el), end=' ') 