from amcp_pylib.core import Client
from pythonosc import dispatcher
from pythonosc import osc_server
import time
import math
import ConfigProvider
import traceback

config = ConfigProvider.getCurrentSettings()

class CasparCGService:
    def __init__(self, sharedData):
        self.sharedData = sharedData

    def start(self):
        try:
            # Establish AMCP Connection
            client = Client()
            client.connect(config['server'], config['port_amcp'])

            # Create OSC Server
            disp = dispatcher.Dispatcher()
            disp.map('/channel/' + str(config['channel']) + '/stage/layer/' + str(config['layer']) + '/file/time', self.handleOSCCommand)

            server = osc_server.ThreadingOSCUDPServer(
                ("0.0.0.0", int(config['port_osc'])), disp)
            print("Serving on {}".format(server.server_address))
            server.serve_forever()
        except:
            print("Fehler: Konnte keine Verbindung zu CasparCG-Server %s:%s herstellen" % (config['server'], config['port_amcp']))
            print(traceback.format_exc())

    def handleOSCCommand(self, *args):
        # args[0] is endpoint
        curTime = args[1]
        totalTime = args[2]
        countdownTime = totalTime - curTime

        formattedTime = time.strftime('%H:%M:%S', time.gmtime(countdownTime))

        # Add Milliseconds manually
	# Divide by 2 to convert from 0 - 100 ms to 0 - 50 frames
        lastDigits = math.trunc((countdownTime - math.trunc(countdownTime)) * 100 / 2)
        if (lastDigits < 10):
            lastDigits = "0" + str(lastDigits)
        formattedTime += ':' + str(lastDigits)

        countDownPercentage = curTime / totalTime * 100

        if totalTime - curTime <= 0.1:
            formattedTime = '00:00:00:00'
            countDownPercentage = 0

        self.sharedData['countDownString'] = formattedTime
        self.sharedData['countDownPercentage'] = countDownPercentage

