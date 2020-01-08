import json
import requests
from firebase import firebase
import datetime
firebase = firebase.FirebaseApplication("https://light-adapt.firebaseio.com/", None)
# db=shelve.open("base")
def makeunix(st_time):
    time_correctly=st_time.split()[1]
    return time_correctly
while True:
    try:
        response = requests.get("http://map.ettu.ru/api/v2/troll/boards/?apiKey=111&order=1").text
        data = json.loads(response)["vehicles"]
        for information in data:
                if information["ROUTE"] =="3":

                        lat=float(information["LAT"])
                        lon=float(information["LON"])
                        board=information["BOARD_ID"]
                        course=information["COURSE"]

                        need='{"gps":{"lat":'+str(lat)+', "lon":'+str(lon)+'}, "board_id":'+board+', "course":'+course+"}"
                        print(need)
                        push = firebase.put("https://light-adapt.firebaseio.com/", str(makeunix(information["ATIME"])),need)
    except:
        pass
