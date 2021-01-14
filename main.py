#!/usr/bin/python
import ScreenService as screen
import ClockService as clock
import CasparCGService as CasparCG
import WebServerService as WebServer
import ShowTimeService as ShowTime
import multiprocessing
import time
import logging

logging.getLogger().setLevel(logging.ERROR)


manager = multiprocessing.Manager()
sharedData = manager.dict()

def startScreen():
    window = screen.ScreenService(sharedData)
    window.start()

def startClock():
    time = clock.ClockService(sharedData)
    time.start()

def startCasparCG():
    server = CasparCG.CasparCGService(sharedData)
    server.start()

def startWebServer():
    server = WebServer.WebServerService(sharedData)
    server.start()

def startShowTime():
    server = ShowTime.ShowTimeService(sharedData)
    server.start()


if __name__ == "__main__":
    screenProcess = multiprocessing.Process(target=startScreen)
    screenProcess.start()

    clockProcess = multiprocessing.Process(target=startClock)
    clockProcess.start()

    casparCGProcess = multiprocessing.Process(target=startCasparCG)
    casparCGProcess.start()

    webServerProcess = multiprocessing.Process(target=startWebServer)
    webServerProcess.start()

    showTimeProcess = multiprocessing.Process(target=startShowTime)
    showTimeProcess.start()

    screenProcess.join()
    clockProcess.join()
    casparCGProcess.join()
    webServerProcess.join()
    showTimeProcess.join()