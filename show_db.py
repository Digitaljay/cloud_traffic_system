import shelve
db=shelve.open("32")
print(db.keys())
for i in db:
    print(i,db[i])
db.close()
