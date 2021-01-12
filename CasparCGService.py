from amcp_pylib.core import Client
from pythonosc import dispatcher
from pythonosc import osc_server
import time
import math

IP = "192.168.1.141"
AMCP_PORT = 5250
OSC_PORT = 6250
CCG_CHANNEL = 1
CCG_LAYER = 10

class CasparCGService:
    def __init__(self, sharedData):
        self.sharedData = sharedData

    def start(self):
        # Establish AMCP Connection
        client = Client()
        client.connect(IP, AMCP_PORT)

        # Create OSC Server
        disp = dispatcher.Dispatcher()
        disp.map('/channel/' + str(CCG_CHANNEL) + '/stage/layer/' + str(CCG_LAYER) + '/file/time', self.handleOSCCommand)

        server = osc_server.ThreadingOSCUDPServer(
            ("0.0.0.0", OSC_PORT), disp)
        print("Serving on {}".format(server.server_address))
        server.serve_forever()

    def handleOSCCommand(self, *args):
        # args[0] is endpoint
        curTime = args[1]
        totalTime = args[2]
        countdownTime = totalTime - curTime

        formattedTime = time.strftime('%H:%M:%S', time.gmtime(countdownTime))

        # Add Milliseconds manually
        lastDigits = math.trunc((countdownTime - math.trunc(countdownTime)) * 100)
        if (lastDigits < 10):
            lastDigits = "0" + str(lastDigits)
        formattedTime += ':' + str(lastDigits)

        if totalTime - curTime <= 0.1:
            formattedTime = '00:00:00:00'

        self.sharedData['countDownString'] = formattedTime

