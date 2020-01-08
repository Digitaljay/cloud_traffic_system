import shelve
db=shelve.open("periods of lights [r]")
# print(db.keys())
for i in db:
    print(i,db[i])
db.close()
