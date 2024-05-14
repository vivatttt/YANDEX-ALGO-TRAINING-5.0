with open('input.txt') as inp:
    n, k = map(int, inp.readline().split())

    freq_part = dict()
    devices = dict()
    value = dict()
    result = dict()
    devices[1] = set(range(1, k + 1)) 
    for part in devices[1]:
        freq_part[part] = 1

    for i in range(2, n + 1):
        devices[i] = set()

    timeslots_passed = 0
    while True:
        requests = dict()
        
        for device in devices.keys():
            
            if device not in result.keys():
                min_part = None
                for i in range(1, k + 1):
                    if i not in devices[device]:
                        if min_part == None:
                            min_part = i
                        else:
                            if freq_part[i] < freq_part[min_part]:
                                min_part = i
                if min_part:
                    download_from = None
                    
                    for i in range(1, n + 1):
                        if i != device:
                            if min_part in devices[i]:
                                if not download_from:
                                    download_from = i
                                    
                                else:
                                    if len(devices[download_from]) > len(devices[i]):
                                        download_from = i
                                        
                    if download_from != None:
                        if download_from in requests.keys():
                            requests[download_from].append((device, min_part))
                        else:
                            requests[download_from] = [(device, min_part)]

        tmp_up = dict()
        tmp_val =dict()

        for uploader in requests.keys():
    
            candidates = requests[uploader]
            
            max_val_key = None
            up = None

            if uploader in value.keys():
                val = value[uploader]

                for item in candidates:
                    key = item[0]
                    cand_valuability = val.get(key, 0)
                    max_valuability = val.get(max_val_key, 0)

                    if max_val_key == None:
                        max_val_key = key
                        up = item[1]
                    else:
                        if cand_valuability > max_valuability:
                            max_val_key = key
                            up = item[1]
                        elif cand_valuability == max_valuability:
                            if len(devices[key]) < len(devices[max_val_key]):
                                max_val_key = key
                                up = item[1]
                            elif len(devices[key]) == len(devices[max_val_key]):
                                if key < max_val_key:
                                    max_val_key = key
                                    up = item[1]


            else:
              
                for item in candidates:
                    key = item[0]
                    
                    if max_val_key == None:
                        max_val_key = key
                        up = item[1]
                    else:
                        if len(devices[key]) < len(devices[max_val_key]):
                            max_val_key = key
                            up = item[1]
                        elif len(devices[key]) == len(devices[max_val_key]):
                            if key < max_val_key:
                                max_val_key = key
                                up = item[1]
                
            if max_val_key in tmp_up:
                tmp_up[max_val_key].add(up)
            else:
                tmp_up[max_val_key] = {up}
          
            if max_val_key in tmp_val:
                tmp_val[max_val_key][uploader] = tmp_val[max_val_key].get(uploader, 0) + 1
            else:
                tmp_val[max_val_key] = {uploader : 1}

            freq_part[up] += 1

        
        for key in tmp_up.keys():
            for el in tmp_up[key]:
                devices[key].add(el)
    
        for key in tmp_val:
            for uploader in tmp_val[key]:
                if key in value:
                    value[key][uploader] = value[key].get(uploader, 0)  + 1
                else:
                    value[key] = {uploader : 1}

        timeslots_passed += 1
       
        for key in devices.keys():
            if len(devices[key]) == k and key not in result.keys():
                result[key] = timeslots_passed
                
                
        if len(result) == n:
            break

res = []
for i in range(2, n + 1):
    res.append(result[i])
print(*res)
