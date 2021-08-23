t = int(input().strip())

periods = []
years = []
for t0 in range(t):
    y1,m1,d1 = [int(i) for i in input().split()]
    if d1 > 1:
        m1 += 1
        if m1 == 13:
            y1 += 1
            m1 = 1
    y2,m2,_ = [int(i) for i in input().split()] # second date does not matter
    periods.append([(y1,m1-1),(y2,m2-1),0]) # months indexed start, finish and index
    years.append((y1,y2))

selected_years = []
for begin,end in sorted(years):
    if selected_years and selected_years[-1][1] >= begin - 1:
        selected_years[-1][1] = max(selected_years[-1][1], end)
    else:
        selected_years.append([begin, end])

def leap_year(year):
    return (year%4 == 0 and year%100 != 0) or year%400 == 0

# Stage #1 - add days mod 7 for unselected years (from December to December)
def add_years(year_start,year_stop):
    global monthstart_day
    for curr_year in range(year_start,year_stop):
        if leap_year(curr_year):
            monthstart_day = (monthstart_day + 2) % 7
        else:
            monthstart_day = (monthstart_day + 1) % 7

def mod7_month(month,year):
    # February
    if month == 2:
        if leap_year(year):
            return 1
        else:
            return 0
    # April, June, September, November
    if month in [4,6,9,11]:
        return 2
    # Everything else
    return 3

# Stage #2 - add days mod 7 for months in selected years, and count Sundays
def add_months(year_start,year_stop):
    global monthstart_day, curr_year
    for curr_year in range(year_start,year_stop+1):
        for curr_month in range(12):
            # add number of days from previous months (e.g. curr_month = 0 (January), add December days 31 (mod 7) = 3)
            monthstart_day = (monthstart_day + mod7_month(curr_month,curr_year)) % 7
            # If Sunday
            if monthstart_day == 0:
                for period in periods:
                    start_date,end_date = period[:2]
                    if start_date <= (curr_year,curr_month) <= end_date:
                        period[2] += 1

# initialize for 1 December 1899 (Friday,5) 
monthstart_day = 5
curr_year = 1899
while selected_years:
    curr_year += 1
    year_start,year_stop = selected_years[0]
    add_years(curr_year,year_start)
    add_months(year_start,year_stop)
    # remove period from list
    selected_years = selected_years[1:]

for period in periods:
    print(period[2])