import os
from flask import Flask

import localsettings

app = Flask(__name__)
app.debug = localsettings.DEBUG

@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
