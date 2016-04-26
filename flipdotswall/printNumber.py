import os
import time
import sys

def print_fd(number):
    i_str = str(int(number))
    i_str = i_str.zfill(3)

    cmd ='cd ./flipdotswall && ./sendImageToFlipdots'
    for char in i_str:
        cmd = cmd + ' font/'+char+'.png'
    os.system(cmd)
