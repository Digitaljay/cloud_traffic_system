import shelve
from firebase import firebase
key="32"
firebase = firebase.FirebaseApplication("https://route-32.firebaseio.com/", None)
db=shelve.open(key)
# print(db.keys())
def makeunix(st_time):
    time_correctly=st_time.split()[1]
    return time_correctly
for i in db:
    lon=db[i][1]
    if lon>=60.639491:
        push = firebase.put("https://route-32.firebaseio.com/", str(makeunix(i)),";".join([str(jjj) for jjj in db[i]]))
        print(i,db[i])
db.close()
