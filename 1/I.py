def isLeap(year):
    if year % 400 == 0:
        return 1
    elif year % 4 == 0 and year % 100 != 0:
        return 1
    return 0


def day_of_month_starts(month, year, day_january_starts_with):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    months = {
        'January' : 31, 
        'February' : 28 + isLeap(year),
        'March' : 31,
        'April' : 30,
        'May' : 31,
        'June' : 30,
        'July' : 31,
        'August' : 31,
        'September' : 30,
        'October' : 31,
        'November' : 30,
        'December' : 31
    }
    s = days.index(day_january_starts_with) - 1

    for cur_month in months.keys():
       
        if cur_month == month:
            break
        s += months[cur_month]
    
    return s % 7 + 1

arr = []

n = int(input())
year = int(input())

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = {
        'January' : 31, 
        'February' : 28 + isLeap(year),
        'March' : 31,
        'April' : 30,
        'May' : 31,
        'June' : 30,
        'July' : 31,
        'August' : 31,
        'September' : 30,
        'October' : 31,
        'November' : 30,
        'December' : 31
}

zeros = [0] * 7
holidays = dict(zip(days, zeros))

for _ in range(n):
    day, month = input().split()
    arr.append((int(day), month))

day_january_starts_with = input()

for day, month in arr:
    offset = day_of_month_starts(month, year, day_january_starts_with)
    holidays[days[(offset + day - 1) % 7]] += 1

holidays[day_january_starts_with] -= 1
if isLeap(year):
    holidays[days[(days.index(day_january_starts_with) + 1) % 7]] -= 1

better = min(holidays.keys(), key=holidays.get)
worst = max(holidays.keys(), key=holidays.get)
print(better, worst)



