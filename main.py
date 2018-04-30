import os
from threading import Timer


def initialization():
    # SHOULD BE 28800 SECS WHICH EQUALS 8 HOURS
    waitingToWater = Timer(10.0, startWatering(0, 1))
    waitingToWater.start()

def startWatering(stack, relayNum):
    os.system(("megaio " + stack + " rwrite " + relayNum + " on"))
    # SHOULD BE 12 SECS
    needToStop = Timer(12.0, stopWatering(stack, relayNum))
    needToStop.start()

def stopWatering(stack, relayNum):
    os.system(("megaio " + stack + " rwrite " + relayNum + " off"))