import datetime
import datetime

from database.storage import get_session
from database.models.scan_event import ScanEvent

from flipdotswall.printNumber import print_fd
from drinks_display.display import Display

class Worker:
    def __init__(self):
        pass

    def __write_db(self, barcode):
        session = get_session()
        ev = ScanEvent(barcode, datetime.datetime.now())
        session.add(ev)
        session.commit()

    def __get_drinks_count(self, date):
        session = get_session()
        result = session.execute("""
          SELECT
            timestamp::date date,
            COUNT(timestamp) amountd
          FROM scanevent
          WHERE timestamp::date = '{today}'
          GROUP BY timestamp::date
        """.format(today=date)).fetchall()

        row = result[0]
        date = row[0]
        amount = row[1]

        return amount

    def __print_flipdots(self, barcode):
        today = datetime.date.strftime(datetime.datetime.now(), '%Y-%m-%d')
        now = today + ' ' +datetime.date.strftime(datetime.datetime.now(), '%H:%M')
        amount = self.__get_drinks_count(today)
        print_fd(amount)

        display = Display()
        display.log(barcode)

        print '|-| '+barcode + ' - '+ str(amount) +' |-|'

    def on_barcode(self, barcode):
        self.__write_db(barcode)
        self.__print_flipdots(barcode)
