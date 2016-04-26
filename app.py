#!/usr/bin/env python
from flask import Flask
import threading

from barcode.barcode_reader import run
from barcode.barcode_worker import Worker

from database.storage import init_db
from database.storage import get_session
from database.models.scan_event import ScanEvent

import datetime
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hi, this is drinks scanner. Have a nice day!'

def start_barcode_scanner_bg():
    worker = Worker()
    t = threading.Thread(
        target=run,
        args=(worker,)
    )
    t.daemon = True
    t.start()

if __name__ == '__main__':
    if(os.geteuid()!= 0):
        print "Please run as root, so we can access the barcode scanner"
        exit(0)

    init_db()

    start_barcode_scanner_bg()
    app.run()
