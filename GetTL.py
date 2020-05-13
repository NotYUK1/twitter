import tweepy
import json, config
import re
import datetime
from pytz import timezone

def get_text(str):
    rem = re.sub('@[a-zA-Z0-9_]*|http.*[a-zA-Z0-9]|#.*\s|#.*$|^RT','',str)
    t = []
    t = re.findall(u'[a-zA-Z0-9ぁ-んァ-ヴーｦ-ﾟ一-龥！？。、々\n]',rem)
    return ''.join(t)

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(config.Consumer_key, config.Consumer_secret)
auth.set_access_token(config.Access_token, config.Access_secret)

api = tweepy.API(auth)

now = datetime.datetime.now(timezone('UTC'))
h = datetime.timedelta(hours=1)
n = now.replace(tzinfo=None)
ago = n - h
f = open("TL.txt", 'wt')
#1ツイートずつループ
for status in api.home_timeline(count=200):
    tm = status.created_at
    if(tm < ago):
        break

    box = re.match("みんなからの匿名質問を募集中",status.text)
    if box != None:
        continue

    text = get_text(status.text)
    f.write(text+'\n')

f.close()