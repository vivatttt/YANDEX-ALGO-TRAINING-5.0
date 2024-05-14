n = int(input())

cord_x = [float("inf"), float("-inf")]
cord_y = [float("inf"), float("-inf")]

for _ in range(n):
    x, y = map(int, input().split())

    cord_x[0] = min(cord_x[0], x)
    cord_x[1] = max(cord_x[1], x)

    cord_y[0] = min(cord_y[0], y)
    cord_y[1] = max(cord_y[1], y)


print(cord_x[0], cord_y[0], cord_x[1], cord_y[1])
