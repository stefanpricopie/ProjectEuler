import datetime

t = int(input().strip())

for t0 in range(t):
    y1,m1,d1 = [int(i) for i in input().split()]
    if d1 > 1:
        m1 += 1
        if m1 == 13:
            y1 += 1
            m1 = 1
    y2,m2,_ = [int(i) for i in input().split()] # second date does not matter
    # Calendar repeats every 400 years
    d_y = y2-y1
    y1 = (y1-1900) % 400 + 1900
    y2 = y1 + d_y
    days = [datetime.date(y1,m1,1)]
    for _ in range(12*(y2-y1)+m2-m1):
        m1 += 1
        if m1 == 13:
            y1 += 1
            m1 = 1
        days.append(datetime.date(y1,m1,1))
    print([day.weekday() for day in days].count(6))