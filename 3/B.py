with open('input.txt', 'r', encoding='utf-8') as inp:

    a = inp.readline().strip()
    b = inp.readline().strip()
    da = dict()
    db = dict()

    for l in a:
        da[l] = da.get(l, 0) + 1

    for l in b:
        db[l] = db.get(l, 0) + 1
        
    
    flag = 1
    for l in da.keys():
        if l not in db.keys():
         
            flag = 0
            break
        else:
            if da[l] != db[l]:
            
                flag = 0
                break
    print('YES' if flag else 'NO')
    
