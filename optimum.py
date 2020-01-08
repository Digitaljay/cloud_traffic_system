import time
import datetime
import shelve
vx=6.4
vy=5.6
# y=0
# x=0
# RED=108
# GREEN=42
finishx=470
finishy=410

db=shelve.open("periods of lights [r]")

for red in range(31,131):
    RED=red
    GREEN=150-red
    db[str(red)]=0
    for first in range(0,150):
        for second in range(0,150):
            print(RED,GREEN,first,second)
            y=0
            x=0

            now_stay_green=max(0,GREEN-first)
            now_stay_red=min(RED,150-first)
            time_now=0
            while x<=finishx and y<=finishy:
                color=1
                # sec=max(0,GREEN-first)
                while now_stay_green>0 and x<=finishx and y<=finishy:
                    # print(int(x),int(y),sec)
                    x+=vx
                    y+=vy
                    time_now+=1
                    now_stay_green-=1
                if x<finishx and y<finishy:
                    color=0
                    time_now+=now_stay_red
                now_stay_green=GREEN
                now_stay_red=RED

            # time_last=datetime.datetime.now()

            x=0
            y=0


            second_time=max(0,GREEN-second)
            now_stay_red=min(RED,150-second)
            now_stay_green=max(0,RED-second)
            while x<=finishx and y<=finishy:
                color=0
                # sec=max(0,GREEN-first)
                while now_stay_red>0 and x<=finishx and y<=finishy:
                    # print(int(x),int(y),sec)
                    x+=vx
                    y+=vy
                    time_now+=1
                    now_stay_red-=1
                if x<finishx and y<finishy:
                    color=0
                    time_now+=now_stay_green
                now_stay_green=GREEN
                now_stay_red=RED
            result_time=max(time_now,second_time)
            # result_time=max(time_last-time_now,time_last_sure-time_last)
            db[str(RED)]=max(db[str(RED)],result_time)
            # print(time_last-time_now)
db.close()
