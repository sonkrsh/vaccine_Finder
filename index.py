import requests
import time
from playsound import playsound
dist = 110047
date = '22-09-2021'
URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(
    dist, date)


def findAvailability():
    counter = 0
    result = requests.get(URL)

    response_json = result.json()
    data = response_json["sessions"]
    for each in data:
        if((each["available_capacity"] > 0) & (each["min_age_limit"] == 18 & (each["name"] != "St Mary Medical Center"))):
            counter += 1
            print(each["name"])
            print(each["pincode"])
            print(each["vaccine"])
            print(each["available_capacity"])
            playsound('/Users/mac/Downloads/police.mp3')
            return True
    if(counter == 0):
        print("No Available Slots")
        return False


while(findAvailability() != True):
    time.sleep(20)
    findAvailability()
