import json
import requests
import shelve
def makeunix(st_time):
    time_correctly=st_time.split()[1]
    return time_correctly
import datetime
# db=shelve.open("base")
while True:
    try:
        response = requests.get("http://map.ettu.ru/api/v2/tram/boards/?apiKey=111&order=1").text
        data = json.loads(response)["vehicles"]
        for information in data:
                # print(type(information["ROUTE"]))
                # print(information["ROUTE"])
                if information["ROUTE"] in ["5","16","20","23","32"]:
                    lat=float(information["LAT"])
                    lon=float(information["LON"])
                    # print(information)
                    if 56.845706<=lat<=56.854187 and lon<=60.645827:
                        db=shelve.open(information["ROUTE"])
                        db[information["ATIME"]]=[lat,lon,information["VELOCITY"]]
                        print(lat,lon,information["ROUTE"])
                        # aska=db[information["ROUTE"]]
                        # towrite={}
                        # time_inf=information["ATIME"]
                        # towrite["lat"]=lat
                        # towrite["lon"]=lon
                        # towrite["speed"]=information["VELOCITY"]
                        # aska[time_inf]=towrite
                        # db[information["ROUTE"]]=aska
                        db.close()
    except:
        pass
