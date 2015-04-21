# -*- coding: utf-8 -*-
"""
Based on: http://nbviewer.ipython.org/github/alexhanna/hse-twitter/blob/master/docs/Collecting%20Twitter%20data%20from%20the%20API%20with%20Python.ipynb
"""

from slistener import SListener
import tweepy

# auth.
# TK: Edit the username and password fields to authenticate from Twitter.
username = 'msw'
password = '1he@rtTw1tter@P1'
# auth = tweepy.auth.BasicAuthHandler(username, password)

# Eventually you'll need to use OAuth. Here's the code for it here.
# You can learn more about OAuth here: https://dev.twitter.com/docs/auth/oauth
API_KEY = 'Sy5rv8DBFp7V9Zk41NBYqEwzM'
API_SECRET = 'WzoX7vs3ud3Wh8mz1WbMIdh30wHMkqB5tXkUtGB0khcMdAxtC2'
ACCESS_TOKEN = '3108551175-S2ZaD281aufhceKUSm13J6zR7XZzBgMEJn87UlK'
ACCESS_TOKEN_SECRET = 'oPVgLTm8pGqQrxlqVMA8qQzADJ7gFwnYKYPlCklgPWSk0'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def main(mode=1):
    # track = ['pizza']
    # follow = []

    listen = SListener(api, 'test')
    stream = tweepy.Stream(auth, listen)

    # on %s users and %s keywords..." % (len(track), len(follow))
    print ("Streaming started, type Ctrl-C to quit")

    try:
        # stream.filter(track = track, follow = follow) # for keywords or users

        # for bounding box LLlong,Lat, URLong, Lat of DC area
        stream.filter(locations=[-78.17, 38.33, -76.36, 39.38])

        # stream.sample()
    except:
        print ("error!")
        stream.disconnect()

if __name__ == '__main__':
    main()
