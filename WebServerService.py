from flask import Flask, request, send_from_directory

PORT = 3000
DIRECTORY = "http/"


class WebServerService:
    def __init__(self, sharedData):
        self.sharedData = sharedData

    def start(self):
        # set the project root directory as the static folder, you can set others.
        app = Flask(__name__)

        @app.route('/')
        def root():
            return send_from_directory(DIRECTORY, 'index.html')

        @app.route('/styles.css')
        def send_css():
            return send_from_directory(DIRECTORY, 'styles.css')
        @app.route('/index.js')
        def send_js():
            return send_from_directory(DIRECTORY, 'index.js')

        app.run(host="0.0.0.0", port=PORT)
            

