import time
import datetime
vx=6.4
vy=5.6
y=0
x=0
RED=108
GREEN=42
finishx=470
finishy=410
time_now=datetime.datetime.now()
while x<=finishx and y<=finishy:
    color=1
    sec=GREEN
    while sec>0 and x<=finishx and y<=finishy:
        print(int(x),int(y),sec)
        x+=vx
        y+=vy
        time.sleep(1)
        sec-=1
    if x<=finishx and y<=finishy:
        color=0
        time.sleep(RED)
time_last=datetime.datetime.now()
print(time_last-time_now)
