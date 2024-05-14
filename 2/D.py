def get_sections(x, y):

    return [((x - 1, y - 1), (x, y - 1)), ((x - 1, y - 1), (x - 1, y)), ((x, y - 1), (x, y)), ((x - 1, y), (x, y))]

n = int(input())
sections = set()
p = 0
for _ in range(n):
    x, y = map(int, input().split())

    secs  = get_sections(x, y)
  
    for sec in secs:
        
        if sec not in sections:
            sections.add(sec)
            p += 1
        else:
            p -= 1
print(p)
