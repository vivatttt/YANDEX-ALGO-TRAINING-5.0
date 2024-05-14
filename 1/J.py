def process_data(data):
    res = []

    for paragraph in data:
        arr = paragraph.split('(image')
    
        cur = []
        for el in arr:
            if ')' in el:
                el = el.replace(')', '')
                el = el.split()
                cur.append(dict())
                img_i = len(cur) - 1
                for val in el:
                    if '=' in val:
                        
                        val = val.split('=')
                        cur[img_i][val[0]] = val[1]
                    else:
                        
                        cur.append(val)
            else:
                
                el = el.split()
                for val in el:
                    cur.append(val)
        res.append(cur)
    return res


def get_fragments(arr, w, y, x):
    res = []
    arr.sort(key = lambda el: el[1])
   
    i = 0
    while i < len(arr):
        
        if y < arr[i][0]:
            if arr[i][1] - x > 0:
    
                res.append([x, arr[i][1]])
            x = arr[i][2] if arr[i][2] > x else x
            i += 1
        else:
            del arr[i]

    if w - x > 0:
        res.append([x, w])
    return res if res else [[x, w]]

def space(x, y, c, surr):
    i = 0
    while i < len(surr):
        if y < surr[i][1]:
            
            if surr[i][0] == x:
                return 0
            
        i += 1
        
    return int(bool(x)) * c

        

def solution(paragraphs, w, h, c):
    surr = []
    arr_pictures = []
    res = []
    floating_x = 0
    floating_y = 0
    y = 0
    for paragraph in paragraphs:
        cur_h = h
        x = 0
        
        

        for el in paragraph:
            free_fragments = get_fragments(arr_pictures, w, y, x)
        
            if type(el) is dict:
                
                if el['layout'] == 'floating':
                    dx = int(el['dx'])
                    dy = int(el['dy'])
                    width = int(el['width'])
                    
                    if floating_x + dx + width <= w and floating_x + dx >= 0:
                        x0 = floating_x + dx
                    elif floating_x + dx + width > w:
                        x0 = w - width
                    else:
                        x0 = 0
                    y0 = floating_y + dy
                    
                    floating_x = x0 + width
                    floating_y = y0
                    res.append((x0, y0))

                elif el['layout'] == 'embedded':
                    width = int(el['width'])
                    height = int(el['height'])
                    i = 0
                    free_fragment = free_fragments[0]
                    
                    while free_fragment[1] - free_fragment[0] < width + space(free_fragment[0], y, c, surr):
                   
                        if i == len(free_fragments) - 1:
                            y += cur_h
                           
                            cur_h = h
                            
                            free_fragments = get_fragments(arr_pictures, w, y, 0)
                            x = free_fragments[0][0]
                            i = 0
                        else:
                            x = free_fragment[1]
                            i += 1
                        free_fragment = free_fragments[i]
                       
                    r = space(free_fragment[0], y, c, surr)
                    res.append((free_fragment[0] + r, y))
                    arr_pictures.append([y + height, free_fragment[0] + r, free_fragment[0] + width])
                
                    x = free_fragment[0] + width + r
                 
                    cur_h = max(cur_h, height)
                    
                    floating_x = x
                    floating_y = y
                    
                elif el['layout'] == 'surrounded':
                    width = int(el['width'])
                    height = int(el['height'])
                    i = 0
                    free_fragment = free_fragments[0]
                   
                    while free_fragment[1] - free_fragment[0] < width:
                        if i == len(free_fragments) - 1:
                            y += cur_h
                            cur_h = h
                            x = 0
                            free_fragments = get_fragments(arr_pictures, w, y, 0)
                          
                            i = 0
                        else:
                            i += 1
                        free_fragment = free_fragments[i]
                        
                    
                    res.append((free_fragment[0], y))
                    arr_pictures.append([y + height, free_fragment[0], free_fragment[0] + width])

                    surr.append((free_fragment[0] + width, y + height))
            
                    x = free_fragment[0] + width
                    
                    floating_x = x
                    floating_y = y
            else:
                
                width = len(el) * c
                free_fragment = free_fragments[0]
                i = 0
                
                while free_fragment[1] - free_fragment[0] < width + space(free_fragment[0], y, c, surr):
                    if i == len(free_fragments) - 1:
                        y += cur_h
                        cur_h = h
                        x = 0
                        free_fragments = get_fragments(arr_pictures, w, y, 0)
                          
                        i = 0
                    else:
                        i += 1
                    
                    free_fragment = free_fragments[i]
               
                x = free_fragment[0] + width + space(free_fragment[0], y, c, surr)
                
                floating_x = x
                floating_y = y
                
        max_emb = 0
        for el in arr_pictures:
            max_emb = max(max_emb, el[0] - y)
        y += max(cur_h, max_emb)
        floating_x = 0
        floating_y = y

    return res


        



with open('input.txt', 'r') as input:

    w, h, c = map(int, input.readline().split())
    paragraphs = []
    cur_string = ''
    for line in input:
        if line.isspace():
            paragraphs.append(cur_string)
            cur_string = ''
        else:
            cur_string += line
    paragraphs.append(cur_string)
    paragraphs = process_data(paragraphs)
    result = solution(paragraphs, w, h, c)


for x, y in result:
    print(x, y)
