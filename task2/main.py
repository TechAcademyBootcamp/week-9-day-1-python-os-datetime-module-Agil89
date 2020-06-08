from datetime import *

# Sample String : Jan 1 2014 2:43PM
# Expected Output : 2014-07-01 14:43:00

time_st = "Jan 1 2014 2:43PM"
print(datetime.strptime(time_st, '%b %d %Y %I:%M%p')+timedelta(6))