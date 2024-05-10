import time

import requests
import json
import pyttsx3
city=input("enter name of the city:")
url=f"https://api.weatherapi.com/v1/current.json?key=a4dcab1c48044399aad130716240905&q={city}"
r=requests.get(url)
print(r.text)
print(type(r.text))
wdic=json.loads(r.text)
print(wdic["current"]["temp_c"])
print(wdic["current"]["temp_f"])
t=wdic["current"]["temp_c"]
w=wdic["current"]["temp_f"]

engine=pyttsx3.init()

engine.say("hi this is weather app")
engine.runAndWait()
time.sleep(1)
engine.say(f"temperature in {city} is {t} in celcius")
engine.say(f"temperature in {city} is {w} in farenheit")
engine.runAndWait()
time.sleep(1)
engine.say("hope you enjoyed this experience of using this app made by hirdesh sharma")
engine.runAndWait()

