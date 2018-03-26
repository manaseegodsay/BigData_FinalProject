import time
from datetime import datetime
import tweepy
import json

auth = tweepy.OAuthHandler('3XGjO3iLMIQIg2v64oESBOi4Z', 'SpV5Y2rmTY96MX55VgiUNXE2EzVFCXslTskFRX8jFI3tvcOpJp')
auth.set_access_token('906966070975746055-YO9WBG5KnmkZi1Q0k42J7BxnsUw9BK3', 'L3NAmTD4rSEUIWqLhVXcqqtNtgL09GtKg9HBTMTA0QK02')

api = tweepy.API(auth)

ids = []
data = json.dumps(ids)
for page in tweepy.Cursor(api.followers_ids, screen_name="melindagates").pages():
    ids.extend(page)
    time.sleep(60)

print (len(ids))
