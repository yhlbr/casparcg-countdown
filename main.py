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

casparCGProcess = None

processes = []

def startScreen():
    window = screen.ScreenService(sharedData)
    processes.append(window)
    window.start()

def startClock():
    time = clock.ClockService(sharedData)
    processes.append(time)
    time.start()

def startCasparCG():
    server = CasparCG.CasparCGService(sharedData)
    processes.append(server)
    server.start()

def startWebServer():
    server = WebServer.WebServerService(sharedData)
    processes.append(server)
    server.start()

def startShowTime():
    server = ShowTime.ShowTimeService(sharedData)
    processes.append(server)
    server.start()

def restartCasparCG():
    casparCGProcess.terminate()
    startCasparCGService()

def startCasparCGService():
    casparCGProcess = multiprocessing.Process(target=startCasparCG)
    processes.append(casparCGProcess)
    casparCGProcess.start()

if __name__ == "__main__":
    screenProcess = multiprocessing.Process(target=startScreen)
    screenProcess.start()

    clockProcess = multiprocessing.Process(target=startClock)
    clockProcess.start()

    startCasparCGService()

    webServerProcess = multiprocessing.Process(target=startWebServer)
    webServerProcess.start()

    showTimeProcess = multiprocessing.Process(target=startShowTime)
    showTimeProcess.start()

    screenProcess.join()
    clockProcess.join()
    casparCGProcess.join()
    webServerProcess.join()
    showTimeProcess.join()