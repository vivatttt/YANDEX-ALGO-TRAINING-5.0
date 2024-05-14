def circle_intersect(x1, y1, x2, y2, r1, r2):

    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if d == 0 and r1 == r2:
        return False
    
    if d > r1 + r2 :
        return False
   
    if d < abs(r1 - r2):
        return False
    k = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
    h = (r1 ** 2 - k ** 2) ** 0.5
  
    x3 = x1 + k * (x2 - x1) / d + h * (y2 - y1) / d     
    y3 = y1 + k * (y2 - y1) / d - h * (x2 - x1) /d 


    x4 = x1 + k * (x2 - x1) / d - h * (y2 - y1) / d
    y4 = y1 + k * (y2 - y1) / d + h * (x2 - x1) / d
        
    return ((x3, y3), (x4, y4))


def isvalid(D, n, arr, t):
    flag = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            x1, y1, v1 = arr[i]
            x2, y2, v2 = arr[j]
            
            r1 = v1 * t
            r2 = v2 * t
            
            k = circle_intersect(x1, y1, x2, y2, r1, r2)
            if k:
                (p_x1, p_y1), (p_x2, p_y2) = k
                
                res = []

                if p_x1 ** 2 + p_y1 ** 2 <= D ** 2 and p_y1 >= 0:
                    flag = 1
                    res.append((p_x1, p_y1))
                
                if p_x2 ** 2 + p_y2 ** 2 <= D ** 2 and p_y2 >= 0:
                    flag = 1
                    res.append((p_x2, p_y2))
             
                
                for b in range(n):
                    xi, yi, vi = arr[b]
                    r = vi * t
                    l = 0
                    while l < len(res):
                        p_x, p_y = res[l]
                        
                        if (p_x - xi) ** 2 + (p_y - yi) ** 2 < r ** 2 and b != i and b != j:
                            del res[l]
                        else:
                            l += 1
                    
                    if not res: 
                        break
                
                if res:
 
                    return (res[0][0], res[0][1])
    
    for a in range(n):
        x, y, v = arr[a]
        r = v * t
        k = circle_intersect(0, 0, x, y, D, r)
        if k:
            res = []
       
            for p_x, p_y in k:
                if p_y >= 0:
                    res.append((p_x, p_y))
                    flag = 1
      
            z = y ** 2 - r ** 2
            if z > 0:
                if x + (y ** 2 - r ** 2) ** 0.5 <= D and x + (y ** 2 - r ** 2) ** 0.5 >= -D:
                    res.append((x + (y ** 2 - r ** 2) ** 0.5, 0))
                if x - (y ** 2 - r ** 2) ** 0.5 <= D and x - (y ** 2 - r ** 2) ** 0.5 >= -D:
                    res.append((x - (y ** 2 - r ** 2) ** 0.5, 0))
                
                flag = 1
            elif z == 0:
                res.append((x, 0))
                flag = 1
          
            for b in range(n):
                xi, yi, vi = arr[b]
                r = vi * t
                l = 0
                while l < len(res):
                    p_x, p_y = res[l]
                        
                    if (p_x - xi) ** 2 + (p_y - yi) ** 2 < r ** 2 and a != b:
                        del res[l]
                    else:
                        l += 1
                    
                if not res: 
                    break
                
            if res:

                return (res[0][0], res[0][1])

    if flag:
 
        return False
    
    for x, y, v in arr:
        r = v * t
        if (D - x) ** 2 + y ** 2 < r ** 2 and (D + x) ** 2 + y ** 2 < r ** 2:

            return False

    return True
                    

                        
                

with open('input.txt', 'r', encoding='utf-8') as inp:
    D, n = map(int, inp.readline().split())
    arr = []
    for _ in range(n):
        arr.append(tuple(map(int, inp.readline().split())))

    t_max = None
    for (x, y, v) in arr:
        s1 = ((D - x) ** 2 + y ** 2) ** 0.5
        s2 = ((D + x) ** 2 + y ** 2) ** 0.5
        if s1 > s2:
            s = s1
            
        else:
            s = s2

        t = s / v
  
        if not t_max:
            t_max = t
        else:
            t_max = max(t_max, t)
            
    l, r = 0, t_max
    
    res = []
    while r - l > 10 ** (-4):
        
        m = (l + r) / 2
        cur = isvalid(D, n, arr, m)
 
        if cur:
            if cur != True:
                res = [m, cur[0], cur[1]]
            l = m
        else:
           r = m
    
print(res[0])
print(res[1], res[2])
