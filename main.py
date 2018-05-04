import os
import time
import schedule
from threading import Timer
from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)
lookup = weather.lookup(2487365)
condition = lookup.condition

needToWaterMore = False
triggerConditions = ["tropical storm", "showers", "hail", "sleet", "mixed rain and hail", "hot", "scattered showers", "scattered showers", "thundershowers"]


def initialization():
    schedule.every().day.at("1:30").do(startWatering, [0, 1])
    schedule.every().hour.do(updateWeather)


def updateWeather():
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
    needToStop = Timer(15.0, stopWatering, [stack,relayNum])
    needToStop.start()
    if needToWaterMore == True:
        waterMore = Timer(20.0, startWatering, [0, 1])
        waterMore.start()


def stopWatering(stack, relayNum):
    os.system("megaio " + str(stack) + " rwrite " + str(relayNum) + " off")
    print("FINISHED WATERING THE PLANTS")
    initialization()


initialization()
while True:
    schedule.run_pending()
    time.sleep(1)