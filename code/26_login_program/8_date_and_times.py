from datetime import datetime


# print(datetime.today())
# now = datetime.today()

"""Date time format codes
%Y - Four digit year
%m - Two digit month
%d - Two digit day
%H - Two digit 24hr
%M - Two digit minute
%S - Two digit second
"""

# # ISO standard minus the milliseconds
# date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(date)
# # American ISO standard minus the milliseconds
# merica = datetime.now().strftime("%A %B %d %y %I:%M%p")
# print(merica)

def ts():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(ts())