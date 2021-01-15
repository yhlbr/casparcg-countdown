from flask import Flask, request, send_from_directory, jsonify
from datetime import datetime
import ConfigProvider as config
import json

import subprocess
import shlex

PORT = 3000
DIRECTORY = "http/"


class WebServerService:
    def __init__(self, sharedData):
        self.sharedData = sharedData

    def start(self):
        # set the project root directory as the static folder, you can set others.
        app = Flask(__name__)

        @app.route('/', methods=['GET', 'POST'])
        def root():
            if request.method == 'POST':
                for key in request.form:
                    config.UpdateSetting(key, request.form.get(key))
                # TODO: Restart CasparCG Process
            return send_from_directory(DIRECTORY, 'index.html')

        @app.route('/styles.css')
        def send_css():
            return send_from_directory(DIRECTORY, 'styles.css')
        @app.route('/index.js')
        def send_js():
            return send_from_directory(DIRECTORY, 'index.js')

        @app.route('/api/v1/show/start')
        def start_show():
            self.sharedData['showStartTime'] = datetime.now()
            self.sharedData['showRunning'] = True
            return "OK"

        @app.route('/api/v1/show/stop')
        def stop_show():
            self.sharedData['showRunning'] = False
            return "OK"

        @app.route('/api/v1/settings')
        def get_settings():
            return jsonify(config.getCurrentSettings())

        @app.route('/shutdown')
        def shutdown():
            cmd = shlex.split("sudo shutdown -h now")
            subprocess.call(cmd)
            return "Wird heruntergefahren..."

        @app.route('/reboot')
        def reboot():
            cmd = shlex.split("sudo reboot")
            subprocess.call(cmd)
            return "Wird neu gestartet..."

        app.run(host="0.0.0.0", port=PORT)
            

