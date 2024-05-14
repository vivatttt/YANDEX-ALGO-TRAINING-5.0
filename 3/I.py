import re

def parse_match_head(line):
    mask = r'(.+) - (.+) (\d+):(\d+)'
    res = re.match(mask, line)
    return res.group(1), res.group(2), int(res.group(3)), int(res.group(4))


def parse_goal(line):
    mask = r'(.+) (\d+)\''
    res = re.match(mask, line)
    return res.group(1), int(res.group(2))




with open('input.txt', 'r', encoding='utf-8') as inp:
    
    lines = inp.read().split('\n')
    if not lines[-1]:
        lines.pop()
    result = []

    total = dict()
    opens = dict()
    on_time = dict()
    squad = dict()
    matches = dict()
    
    i = 0
    cnt = 0
    while i < len(lines):
        line = lines[i]
        if ':' in line:
            # обрабатываем начало матча
            team1, team2, score1, score2 = parse_match_head(line)

            matches[team1] = matches.get(team1, 0) + 1
            matches[team2] = matches.get(team2, 0) + 1

            if team1 in total.keys():
                total[team1] = (total[team1][0] + score1, total[team1][1] + 1)
            else:
                total[team1] = (score1, 1)
            
            if team2 in total.keys():
                total[team2] = (total[team2][0] + score2, total[team2][1] + 1)
            else:
                total[team2] = (score2, 1)

            if team1 not in squad:
                squad[team1] = set()
            if team2 not in squad:
                squad[team2] = set()

            first_scored_1 = None
            for j in range(i + 1, i + score1 + 1):
                line = lines[j]
                name, minute = parse_goal(line)

                squad[team1].add(name)
                if not first_scored_1:
                    first_scored_1 = (name, minute)
                if name in total:
                    total[name] = (total[name][0] + 1, total[name][1])
                else:
                    total[name] = (1, 0)
                # обрабатывваем минуты
                if name in on_time:
                    on_time[name][minute] = on_time[name].get(minute, 0) + 1
                else:
                    on_time[name] = {minute:1}               

 
            first_scored_2 = None
            i += score1
            for j in range(i + 1, i + score2 + 1):
                line = lines[j]
                name, minute = parse_goal(line)

                squad[team2].add(name)
                if not first_scored_2:
                    first_scored_2 = (name, minute)
                
                if name in total:
                    total[name] = (total[name][0] + 1, total[name][1])
                else:
                    total[name] = (1, 0)
                
                # обрабатывваем минуты
                if name in on_time:
                    on_time[name][minute] = on_time[name].get(minute, 0) + 1
                else:
                    on_time[name] = {minute:1} 

            # обрабатываем первого забившего
            if first_scored_1 and first_scored_2:
                if first_scored_1[1] < first_scored_2[1]:
                    opens[team1] = opens.get(team1, 0) + 1
                    opens[first_scored_1[0]] = opens.get(first_scored_1[0], 0) + 1
                else:
                    opens[team2] = opens.get(team2, 0) + 1
                    opens[first_scored_2[0]] = opens.get(first_scored_2[0], 0) + 1
            elif first_scored_1:
                opens[team1] = opens.get(team1, 0) + 1
                opens[first_scored_1[0]] = opens.get(first_scored_1[0], 0) + 1
            elif first_scored_2:
                opens[team2] = opens.get(team2, 0) + 1
                opens[first_scored_2[0]] = opens.get(first_scored_2[0], 0) + 1

            # добавляем всем участникам матча + 1 сыгранный матч
            for player in squad[team1]:
                if player in total:
                    total[player] = (total[player][0], matches[team1])
                
            for player in squad[team2]:
                if player in total:
                    total[player] = (total[player][0], matches[team2])
            
            i += score2 + 1
        else:
            
            # обрабатываем запрос
            if 'Total goals' in line:
                if 'Total goals by' in line:
                    mask = r'Total goals by (.+)'
                else:
                    mask = r'Total goals for (.+)'
                res = re.match(mask, line)
                name = res.group(1)
                if name in total:
                    result.append(total[name][0])
                else:
                    result.append(0)
                
            elif 'Mean goals per game' in line:
                if 'Mean goals per game by' in line:
                    mask = r'Mean goals per game by (.+)'
                else:
                    mask = r'Mean goals per game for (.+)'
                res = re.match(mask, line)
                name = res.group(1)
                result.append(total[name][0]/total[name][1])
                
            elif 'Goals on minute' in line:
                mask = r'Goals on minute (\d+) by (.+)'
                res = re.match(mask, line)
                minute = int(res.group(1))
                name = res.group(2)
                

                if name in on_time:
                    result.append(on_time[name].get(minute, 0))
                else:
                    result.append(0)
                
            elif 'Goals on first' in line:
                mask = r'Goals on first (\d+) minutes by (.+)'
                res = re.match(mask, line)
                t = int(res.group(1))
                name = res.group(2)

                if name in on_time:
                    mins = on_time[name]
                    r = 0
                    for m in mins.keys():
                        if m <= t:
                            r += mins[m]
                    result.append(r)
                else:
                    result.append(0)
            elif 'Goals on last' in line:
                mask = r'Goals on last (\d+) minutes by (.+)'
                res = re.match(mask, line)
                t = int(res.group(1))
                name = res.group(2)

                if name in on_time:
                    mins = on_time[name]
                    r = 0
                    for m in mins.keys():
                        if m >= 91 - t:
                            r += mins[m]
                    result.append(r)
                else:
                    result.append(0)
            else:
                mask = r'Score opens by (.+)'
                res = re.match(mask, line)
                name = res.group(1)

                result.append(opens.get(name, 0))                    
            i += 1
            

for el in result:
    print(el)