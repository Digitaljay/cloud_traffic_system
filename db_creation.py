import shelve
db=shelve.open("base")
db["5"]={}
db["16"]={}
db["20"]={}
db["23"]={}
db["32"]={}
db.close()
