"""Alarm Tunes - Play random YouTube video at given time passed as arguments
   ex: alarm_tunes.py --h 1 --m 13 --p pm
"""

import argparse
import datetime
import sys
import webbrowser
import time
from random import randint

def get_randomvideo():
  """get a list of videos from text file"""
  with open('songs.txt') as songs:
    lines = songs.readlines()
  random_num = randint(1, len(lines))
  return lines[random_num]

def set_time(h,m,p):
  if p == 'PM' or p =='pm':
    h = h + 12
  sleep_Time = str(datetime.time(h,m))
  return sleep_Time

if __name__ == "__main__":

  parser = argparse.ArgumentParser(description='Let\'s set the time ')
  parser.add_argument('--h', type=int, dest='hour', required=True, \
                      help='Type an integer for the hours.')
  parser.add_argument('--m', dest='minute', type=int, required=True, \
                      help='Type an integer for the minutes.')
  parser.add_argument('--p', dest='period', required=True, \
                      help='Type a string for the periods am/pm')
  args = parser.parse_args()
  sleep_Time = set_time(args.hour, args.minute, args.period)
  current_Time = time.strftime("%H:%M:%S")

  while (cmp(sleep_Time,current_Time) != 0):
    current_Time = time.strftime("%H:%M:%S")
    time.sleep(1)
  if (cmp(sleep_Time,current_Time) == 0):
    url = get_randomvideo()
    webbrowser.open(url, new=2, autoraise=True)
