import tweepy
import time
import csv
from datetime import datetime

auth = tweepy.OAuthHandler('3XGjO3iLMIQIg2v64oESBOi4Z', 'SpV5Y2rmTY96MX55VgiUNXE2EzVFCXslTskFRX8jFI3tvcOpJp')
auth.set_access_token('906966070975746055-YO9WBG5KnmkZi1Q0k42J7BxnsUw9BK3',
                      'L3NAmTD4rSEUIWqLhVXcqqtNtgL09GtKg9HBTMTA0QK02')

api = tweepy.API(auth, wait_on_rate_limit=True)

ScreenName = "melindagates"

followers =[]
for user in tweepy.Cursor(api.followers, screen_name=ScreenName, count=10000).items():
    print(user.screen_name)
    followers.append([user.screen_name.encode("utf-8")])
    time.sleep(0.5)

with open('%s_followers.csv' % str(ScreenName), 'w') as f:
    writer = csv.writer(f)
    writer.writerows(followers)