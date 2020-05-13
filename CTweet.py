import tweepy
import sys
import re
import json, Sconfig
import GenerateText

twitter = Sconfig.CreateOAuthSession()
url = "https://api.twitter.com/1.1/statuses/update.json"

generator = GenerateText.GenerateText()
tweet = generator.generate()
params = {"status" : tweet}
twitter.post(url, params = params)