def check(x, y, p, help_p):
    count_base = 0
    flag_base = 1

    while x > 0:
        if y > 0:
         
            if  y >= x:
                y -= x
            else:
                
                p -= (x - y)
                y = 0
            
            x -= p
        else:
            x_attacks_enemies = p if x >= p else x
            x_attacks_base = x - x_attacks_enemies
          
            y -= x_attacks_base
            p -= x_attacks_enemies

            x -= p

        count_base += 1
        if y > 0:
            p += help_p

        if (y <= 0 and p <= 0) or (x == p and y > 0):
            break

    if y > 0 or p > 0:
        flag_base = 0

    if flag_base:
        return count_base
    
    return None
    
x = int(input())
y = int(input())
p = int(input())


flag = 1
count = 1
y -= x
phi = 1.61

help_p = p
minn = float("inf")

if y <= 0:
    print(count)
else:

    while x > 0:
        cur_res = check(x, y, p, help_p)
        if cur_res:
            cur_res += count
            if cur_res < minn:
                minn = cur_res
            
        x_attacks_enemies = p if x >= p else x
        x_attacks_base = x - x_attacks_enemies
           
        y -= x_attacks_base
        p -= x_attacks_enemies

        x -= p

        count += 1
        if y > 0:
            p += help_p

        if y <= 0 and p <= 0 or (x == p and y > 0):
            break
    

    if minn != float("inf"):
        print(minn)
    else:
        print(-1)