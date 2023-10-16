import datetime

date1 = [int(x) for x in input().split('.')]
date2 = [int(x) for x in input().split('.')]
p = int(input())
for d in [date1, date2]:
    d.reverse()

dt1 = datetime.date(*date1)
dt2 = datetime.date(*date2)
date_delta = dt2 - dt1
days = date_delta.days

s = (2 * p + (days)) * (days + 1) / 2
print(round(s))




