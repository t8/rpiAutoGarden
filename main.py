import os
import time
import schedule
from threading import Timer
from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)
lookup = weather.lookup(2487365)
condition = lookup.condition

needToWaterMore = True
triggerConditions = ["tropical storm", "showers", "hail", "sleet", "mixed rain and hail", "scattered showers", "scattered showers", "thundershowers"]


def updateWeather():
    global needToWaterMore
    global lookup
    global condition
    lookup = weather.lookup(2487365)
    condition = lookup.condition
    lowerCaseCondition = condition.text.lower()

    if triggerConditions.count(lowerCaseCondition) > 0:
        needToWaterMore = False
    else:
        needToWaterMore = True


def startWatering(stack, relayNum):
    os.system("megaio " + str(stack) + " rwrite " + str(relayNum) + " on")
    print("NOW WATERING THE PLANTS")
    needToStop = Timer(15.0, stopWatering, [stack, relayNum])
    needToStop.start()
    if needToWaterMore:
        schedule.every().day.at('15:30').do(startWatering, [stack, relayNum]).tag('extra-cycle')
    else:
        schedule.clear('extra-cycle')


def stopWatering(stack, relayNum):
    os.system("megaio " + str(stack) + " rwrite " + str(relayNum) + " off")
    print("FINISHED WATERING THE PLANTS")


schedule.every().day.at("1:30").do(startWatering, [0, 1])
schedule.every().hour.do(updateWeather)
while True:
    schedule.run_pending()
    time.sleep(1)