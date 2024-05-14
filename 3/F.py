with open('input.txt', 'r', encoding='utf-8') as inp:
    d = set(inp.readline().split())
    words = list(inp.readline().split())

    for i in range(len(words)):
        rep = words[i]
        sl = ''
        for letter in words[i]:
            sl += letter
            if sl in d:
                rep = sl
                break
            
        words[i] = rep

print(*words)