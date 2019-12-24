import shelve
db=shelve.open("base")
for i in db:
    print(i,db[i])
db.close()
