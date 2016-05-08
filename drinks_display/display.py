import urllib
import urllib2

class Display(object):
    def __init__(self):
        pass

    def log(self, msg):
        query = urllib.urlencode({
            'msg': msg
        })
        urllib2.urlopen("http://192.168.3.231:5000/?"+query).read()
