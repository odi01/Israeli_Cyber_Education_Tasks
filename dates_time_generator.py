import itertools


# 1
def gen_secs():
    second = 0
    while second < 60:
        yield second
        second += 1

# 2
def gen_minutes():
    yield from gen_secs()

# 3
def gen_hours():
    hour = 0
    while hour < 24:
        yield hour
        hour += 1 

# 4
def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, second)

# 5
def gen_years(start=2019):
    while True:
        yield start
        start += 1

# 6
def gen_months():
    for month in range(1, 13):
        yield month

# 7
def gen_days(month, leap_year=True):
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month != 2:
        yield months[month]
    elif month == 2 and leap_year is True:
        yield 29
    elif month == 2 and leap_year is False:
        yield 28

# 8
def gen_date(year=2019):
    for years in gen_years(year):
        for month in gen_months():
            for days in gen_days(month):
                for day in range(1, days + 1):
                    for time in gen_time():
                        yield "%02d/%02d/%02d %s" % (day, month, years, time)



seconds = gen_secs()
minutes = gen_minutes()
hours = gen_hours()
full_day = gen_time()
years = gen_years()
months = gen_months()
month_days = gen_days(2)
date_n_time = gen_date()



# 9
count = 0
for time in date_n_time:
    if (count == 1000000):
        print(time)
        count = 0
    count += 1