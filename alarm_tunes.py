"""Alarm Tunes - Play random YouTube video at given time in hours"""

import sys
import webbrowser
from time import sleep
from random import randint

def get_randomvideo ():
  """get a list of videos from text file"""
  with open('songs.txt') as songs:
    lines = songs.readlines()
  random_num = randint(0, len(lines))
  return lines[random_num]

hours = float(sys.argv[1]) * 3600.0
sleep(hours)

url = get_randomvideo()
webbrowser.open(url, new=2, autoraise=True)




