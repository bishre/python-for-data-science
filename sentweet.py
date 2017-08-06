import tweepy
from textblob import TextBlob
import csv

consumer_key = 'g9XrU0IotUWBBqNTofa3IvYb6'
consumer_secret = 'Uv0qvkwo0UWkFuAFgOdC7KCSppSISiRhhfPr6nHBvb9HOIa9sr'

access_token = '27202982-mC8RQQ4QCJErPH8LIpjKGnAuJSQtT45u9C3xnKkMl'
access_token_secret = 'itHl6VrEIbPJSdchu27WMxwDOsQtwtPhxRvc598mWrgWT'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

tweet_list = []

write_file = 'tweets.csv'

for tweet in public_tweets:
    tweets=tweet.text
    analysis = TextBlob(tweet.text)
    tweet_list.append(tweets)

print (tweet_list)
print (len(tweet_list))
print (type(analysis))

with open(write_file, 'w', encoding="utf-8") as output:
	writer = csv.writer(output, delimiter=',') 
	for twt in tweet_list:
		#twt=twt.encode('utf-8')
		writer.writerow([twt])
