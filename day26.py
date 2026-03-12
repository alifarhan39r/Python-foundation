import time
t=time.strftime('%H:%M:S')
hour=int(time.strftime('%H'))
hour=int(input( 'enter hour'))
print(hour)

if(hour>=0 and hour<12):
    print("Good Morning Farhan")
elif(hour>=12 and hour<17):
    print("Good Afternoon Farhan")
if(hour>=17 and hour<24):
    print("Good Night Farhan")