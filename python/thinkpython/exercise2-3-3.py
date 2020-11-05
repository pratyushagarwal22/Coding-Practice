'''If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?'''

h = 6
m = 52
s = 0
t = (8*2)+(3*7)
s = (15*2)+(12*3)

# getting the total number of minutes
m = m + (s//60) + t

# getting the final value for seconds 
s = s%60

# getting the final value for hours
h = h + (m//60)

# getting the final value for minutes
m = m%60

print('Final Value for time is: ')
print('Hours: ',h)
print('Minutes: ',m)
print('Seconds: ',s)

