import os
import time
import schedule
from threading import Timer
from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)
lookup = weather.lookup(2487365)
condition = lookup.condition

needToWaterMore = False


def initialization():
    schedule.every().day.at("10:30").do(startWatering, [0, 1])
    update()


def update():
    lookup = weather.lookup(2487365)
    condition = lookup.condition
    if lookup.forecast.high > 75:
        needToWaterMore = True


def startWatering(stack, relayNum):
    os.system("megaio " + str(stack) + " rwrite " + str(relayNum) + " on")
    os.system("echo 'NOW WATERING THE PLANTS'")
    # SHOULD BE 12 SECS
    needToStop = Timer(12.0, stopWatering, [stack,relayNum])
    needToStop.start()
    if needToWaterMore == True:
        waterMore = Timer(20.0, startWatering, [0, 1])
        waterMore.start()


def stopWatering(stack, relayNum):
    os.system("megaio " + str(stack) + " rwrite " + str(relayNum) + " off")
    os.system("echo 'JUST FINISHED WATERING THE PLANTS'")
    initialization()


initialization()
while True:
    schedule.run_pending()
    time.sleep(1)
    update()