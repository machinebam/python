#!/usr/bin/python
import os
import time
from twython import TwythonStreamer
    
# Search terms
RED = '#science,#yes,#fun'
BLUE = '#perth,#music,#movies,#wa'

TERMS = RED+","+BLUE

# Create lists
RED_LIST = RED.split(",")
BLUE_LIST = BLUE.split(",")

# LED Sleep Time
SLEEP_TIME = 0.5
    
# Twitter application authentication
APP_KEY = '#########################'
APP_SECRET = '#########################'
OAUTH_TOKEN = '#########################'
OAUTH_TOKEN_SECRET = '#########################'
    
# Setup callbacks from Twython Streamer
class RedVsBlueStreamer(TwythonStreamer):
  def on_success(self, data):
    if 'text' in data:
      s = data['text'].encode('utf-8')
      print s
      print 
      alert(s)
   
def alert(s):
  for i in range(len(RED_LIST)):
    RED_HASHTAG = RED_LIST[i]
    if RED_HASHTAG in s.lower(): os.system('omxplayer smell.wav')
  for i in range(len(BLUE_LIST)):
    BLUE_HASHTAG = BLUE_LIST[i]
    if BLUE_HASHTAG in s.lower(): os.system('omxplayer keep-the-change.wav')
  
  #else:  error()
  time.sleep(SLEEP_TIME)
  
  return
    
# Setup GPIO as output

  
# Create streamer
try:
  stream = RedVsBlueStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
  stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
  GPIO.cleanup()