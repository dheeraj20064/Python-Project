import requests
import datetime

parameter={
    "lat":12.586210,
    "lng":75.080383,
    "formatted":0
}

response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
sunrise=response.json()["results"]["sunrise"]
sunset=response.json()["results"]["sunset"]
morning=(sunrise.split("T")[1])
evening=(sunset.split("T")[1])
hour1=morning.split(":")[0]
hour2=evening.split(":")[0]
print(hour1)
print(hour2)
print(datetime.datetime.now().hour)
