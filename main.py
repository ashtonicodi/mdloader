__author__ = 'Ashton'

import datetime
import foolib
import urllib.request as urlrequest
from downloader.dwdtypes import files
from downloader.dwdfoo.rqstfoo import *

"""
datetime_now = datetime.datetime.now()
create_time = str(datetime_now.day) + '-' + str(datetime_now.month) + \
    '-' + str(datetime_now.year) + '_' + str(datetime_now.hour) + ':' + str(datetime_now.minute) + \
    ':' + str(datetime_now.second)
"""

if __name__ == "__main__":
    while True:
        if not check_connection():
            print('Internet connection is failed!')
        cmd_line = input('Enter post id: ')
        if cmd_line == 'exit': break

        audio_objects = foolib.get_audio_list(cmd_line)
        foolib.dwd_audio_files(audio_objects)