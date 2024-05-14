def rook(field, i, j):
    i0, j0 = i - 1, j - 1
    while i0 >= 0:
        if field[i0][j] in ('R', 'B'):
            break
        field[i0][j] = '.'
        i0 -= 1
    while j0 >= 0:
        if field[i][j0] in ('R', 'B'):
            break
        field[i][j0] = '.'
        j0 -= 1
    i0, j0 = i + 1, j + 1
    while i0 < 8:
        if field[i0][j] in ('R', 'B'):
            break
        field[i0][j] = '.'
        i0 += 1
    while j0 < 8:
        if field[i][j0] in ('R', 'B'):
            break
        field[i][j0] = '.'
        j0 += 1
    return field
            

def bishop(field, i, j):
    i0, j0 = i - 1, j + 1

    while i0 >= 0 and j0 < 8:
        if field[i0][j0] in ('R', 'B'):
            break
        field[i0][j0] = '.'
        i0 -= 1
        j0 += 1
    
    i0, j0 = i + 1, j - 1

    while j0 >= 0 and i0 < 8:
        if field[i0][j0] in ('R', 'B'):
            break
        field[i0][j0] = '.'
        i0 += 1
        j0 -= 1
    
    i0, j0 = i - 1, j - 1

    while i0 >= 0 and j0 >= 0:
        if field[i0][j0] in ('R', 'B'):
            break
        field[i0][j0] = '.'
        i0 -= 1
        j0 -= 1
    
    i0, j0 = i + 1, j + 1

    while j0 < 8 and i0 < 8:
        if field[i0][j0] in ('R', 'B'):
            break
        field[i0][j0] = '.'
        i0 += 1
        j0 += 1
    return field

    

field = []

for i in range(8):
    field.append(list(input().strip()))

for i in range(8):
    for j in range(8):
        if field[i][j] == 'R':
            field = rook(field, i, j)
        if field[i][j] == 'B':
            field = bishop(field, i, j)
s = 0
for el in field:
    s += el.count('*')
print(s)

