import os
import json
from flask import Flask

import localsettings

app = Flask(__name__)
app.debug = localsettings.DEBUG

@app.route('/')
def index():
    api_payload = open('api_payload.json', 'r')
    api_data = api_payload.read()
    return api_data

if __name__ == '__main__':
    app.run()
