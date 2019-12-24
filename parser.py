import json
import requests
import shelve
response = requests.get("http://map.ettu.ru/api/v2/tram/boards/?apiKey=111&order=1").text
data = json.loads(response)["vehicles"]
db=shelve.open("base")
for information in data:
    # print(information["ROUTE"])
    if information["ROUTE"] in ["5","16","20","23","32"]:
        lat=float(information["LAT"])
        lon=float(information["LON"])
        if 56.845706<=lat<=56.854187 and lon<=60.645827:
            aska=db[information["ROUTE"]]
            towrite={}
            time_inf=information["ATIME"]
            towrite["lat"]=information["LAT"]
            towrite["lon"]=information["LON"]
            towrite["speed"]=information["VELOCITY"]
            aska[time_inf]=towrite
            db[information["ROUTE"]]=aska
db.close()
