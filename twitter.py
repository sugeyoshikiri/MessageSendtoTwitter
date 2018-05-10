# -*- coding:utf-8 -*-
import json
from requests_oauthlib import OAuth1Session

config = json.load(open('config.json', 'r'))
twConsumerKey = config['twConsumerKey']
twConsumerSecret = config['twConsumerSecret']
twToken = config['twToken']
twTokenSecret = config['twTokenSecret']

twitter = OAuth1Session(twConsumerKey, twConsumerSecret, twToken, twTokenSecret)

url = "https://api.twitter.com/1.1/statuses/update.json"

twmsg = {"status" : "hello world"}

req = twitter.post(url, params = twmsg)

if req.status_code == 200:
    print("Succeed!")
else:
    print("ERROR : %d"% req.status_code)
