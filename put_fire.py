import shelve
from firebase import firebase
key="5"
firebase = firebase.FirebaseApplication("https://light-adapt.firebaseio.com/", None)
db=shelve.open(key)
# print(db.keys())
def makeunix(st_time):
    time_correctly=st_time.split()[1]
    return time_correctly
for i in db:
    push = firebase.put("https://light-adapt.firebaseio.com/-LwYM8VBC4e3a4hHf5S9", str(makeunix(i)),";".join([str(jjj) for jjj in db[i]]+[key]))
    print(i,db[i])
db.close()
