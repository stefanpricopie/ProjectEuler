t = int(input().strip())

results = [0]*t
max_y2 = 0
periods = []
for t0 in range(t):
    y1,m1,d1 = [int(i) for i in input().split()]
    if d1 > 1:
        m1 += 1
        if m1 == 13:
            y1 += 1
            m1 = 1
    y2,m2,_ = [int(i) for i in input().split()] # second date does not matter
    max_y2 = max(y2,max_y2)
    periods.append([(y1-1900)*12+m1,(y2-1900)*12+m2,0]) # months indexed start, finish and Sunday counts

def leap_year(year):
    return (year%4 == 0 and year%100 != 0) or year%400 == 0

# nr of days in the total of i (December,January,...,November) months mod 7 for leap and non leap years
mod7_leap =    [3,6,0,3,5,1,3,6,2,4,0,2]
mod7_nonleap = [3,6,6,2,4,0,2,5,1,3,6,1]

# initialize for 1 December 1899 (Friday - 5) 
monthstart_year = [5]
curr_month = 0
for year in range(1900,max_y2+1):
    december1 = monthstart_year[-1]
    # (Jan to December)
    if leap_year(year):
        monthstart_year = [(mod7+december1)%7 for mod7 in mod7_leap]
    else:
        monthstart_year = [(mod7+december1)%7 for mod7 in mod7_nonleap]
    
    for month,day1 in enumerate(monthstart_year):
        if day1 == 0:
            for period in periods:
                if period[0] <= curr_month+month+1 <= period[1]:
                    period[2] += 1
                    x = 1
    curr_month += 12
for period in periods:
    print(period[2])