import urllib
import urllib2

class Display(object):
    def __init__(self):
        pass

    def log(self, msg):
        query = urllib.urlencode({
            'barcode': msg
        })
        urllib2.urlopen("http://drinks-touch:5000/barcode_scanned?"+query).read()
