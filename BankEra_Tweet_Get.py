# -*- coding: utf-8 -*-

from twitter import Twitter, OAuth
import codecs
import sys
import types

t = Twitter(auth=OAuth(
    '935058768563339265-7eIsN2892DRYL6tCrTjzPGnySQQUHfr',
    'G3xDy4lUsRBQbR3GQ1ZEF7ankZgNY64gBpf7x0edPwBxF',
    'xMzUeWmIimG83P9QMhFnENCG4',
    'REDBG6CH9LkiR5ACBgB5hNBEYnwP00Als7TLi39WZCSdS3qLcG'
))

remain = True 
userTweets = [] 
max_id = '976364667172982784'
remainNum = 0
numberOfTweets = 1
count = 1
while remain:
    aTimeLine = t.statuses.user_timeline(user_id = '908504581797113856', count=count, max_id=max_id)
    for tweet in aTimeLine:
        userTweets.append(tweet['text'])
    max_id = aTimeLine[-1]['id']-1
    remainNum = numberOfTweets - len(userTweets)
    count = remainNum
    if len(userTweets)+1 > numberOfTweets:
        print str(userTweets).decode("string-escape")
        remain = False

