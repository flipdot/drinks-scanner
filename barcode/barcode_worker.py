from database.storage import get_session
from database.models.scan_event import ScanEvent

import datetime

class Worker:
    def __init__(self):
        pass

    def __write_db(self, barcode):
        session = get_session()
        ev = ScanEvent(barcode, datetime.datetime.now())
        session.add(ev)
        session.commit()

    def __print_flipdots(self, barcode):
        print '|-| '+barcode+' |-|'

    def on_barcode(self, barcode):
        self.__write_db(barcode)
        self.__print_flipdots(barcode)
