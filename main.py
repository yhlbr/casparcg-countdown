#!/usr/bin/python
import ScreenService as screen
import ClockService as clock
import CasparCGService as CasparCG
import WebServerService as WebServer
import ShowTimeService as ShowTime
import multiprocessing
import time
import logging
import signal

logging.getLogger().setLevel(logging.ERROR)


manager = multiprocessing.Manager()
sharedData = manager.dict()

processes = []

def startScreen():
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    window = screen.ScreenService(sharedData)
    window.start()

def startClock():
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    time = clock.ClockService(sharedData)
    time.start()

def startCasparCG():
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    server = CasparCG.CasparCGService(sharedData)
    server.start()

def startWebServer():
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    server = WebServer.WebServerService(sharedData)
    server.start()

def startShowTime():
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    server = ShowTime.ShowTimeService(sharedData)
    server.start()


if __name__ == "__main__":
    screenProcess = multiprocessing.Process(target=startScreen)
    processes.append(screenProcess)
    screenProcess.start()

    clockProcess = multiprocessing.Process(target=startClock)
    processes.append(clockProcess)
    clockProcess.start()

    casparCGProcess = multiprocessing.Process(target=startCasparCG)
    processes.append(casparCGProcess)
    casparCGProcess.start()

    webServerProcess = multiprocessing.Process(target=startWebServer)
    processes.append(webServerProcess)
    webServerProcess.start()

    showTimeProcess = multiprocessing.Process(target=startShowTime)
    processes.append(showTimeProcess)
    showTimeProcess.start()

    try:
        screenProcess.join()
        clockProcess.join()
        casparCGProcess.join()
        webServerProcess.join()
        showTimeProcess.join()
    except KeyboardInterrupt:
        print("Stopping Services...")
        for p in processes:
            p.terminate()