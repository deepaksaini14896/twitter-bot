import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("key", "key")
auth.set_access_token("token", "token")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

searches='covid19'
no_of_tweets=10

for tweet in tweepy.Cursor(api.search,searches).items(no_of_tweets):
	try:
		tweet.favorite()
		print("you've liked the Tweet")
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break
