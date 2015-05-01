# -*- coding: utf-8 -*-
"""
Based on: http://nbviewer.ipython.org/github/alexhanna/hse-twitter/blob/master/docs/Collecting%20Twitter%20data%20from%20the%20API%20with%20Python.ipynb
"""

from slistener import SListener
import tweepy

from geobbox.settings import (
    API_KEY, API_SECRET,
    ACCESS_TOKEN, ACCESS_TOKEN_SECRET
    )

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def main(mode=1):
    listen = SListener(api, 'test')
    stream = tweepy.Stream(auth, listen)

    print ("Streaming started, type Ctrl-C to quit")

    try:
        # for bounding box LLlong,Lat, URLong, Lat of DC area
        stream.filter(locations=[-78.17, 38.33, -76.36, 39.38])

        # stream.sample()
    except:
        print ("error!")
        stream.disconnect()

if __name__ == '__main__':
    main()
