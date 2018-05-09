import os
import time
import  datetime as dt
import schedule
from threading import Timer
from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)
lookup = weather.lookup(2487365)
condition = lookup.condition

needToWaterEarly = True
needToWaterMore = True
triggerConditions = ["tropical storm", "showers", "hail", "sleet", "mixed rain and hail", "scattered showers", "thundershowers"]


def updateWeather():
    global needToWaterEarly
    global needToWaterMore
    global lookup
    global condition
    lookup = weather.lookup(2487365)
    condition = lookup.condition
    lowerCaseCondition = condition.text.lower()

    if triggerConditions.count(lowerCaseCondition) > 0 and dt.datetime.today().hour == 7:
        needToWaterEarly = False
    else:
        needToWaterEarly = True

    if triggerConditions.count(lowerCaseCondition) > 0 and dt.datetime.today().hour == 18:
        needToWaterMore = False
    else:
        needToWaterMore = True


def startWatering(stack, relayNum):
    if needToWaterEarly and dt.datetime.today().hour == 7:
        os.system("megaio " + str(stack) + " rwrite " + str(relayNum) + " on")
        print("NOW WATERING THE PLANTS AT 7:00 AM")
        needToStop = Timer(150.0, stopWatering, [stack, relayNum])
        needToStop.start()
    else:
        print("SKIPPING EARLY WATER CYCLE: " + condition.text)

    if needToWaterMore and dt.datetime.today().hour == 18:
        os.system("megaio " + str(stack) + " rwrite " + str(relayNum) + " on")
        print("NOW WATERING THE PLANTS AT 6:30 PM")
        needToStop = Timer(150.0, stopWatering, [stack, relayNum])
        needToStop.start()
    else:
        print("SKIPPING LATE WATER CYCLE: " + condition.text)


def stopWatering(stack, relayNum):
    os.system("megaio " + str(stack) + " rwrite " + str(relayNum) + " off")
    print("FINISHED WATERING THE PLANTS")


schedule.every().day.at("7:10").do(startWatering, 0, 1)
schedule.every().day.at("18:30").do(startWatering, 0, 1)
schedule.every().hour.do(updateWeather)
while True:
    schedule.run_pending()
    time.sleep(1)