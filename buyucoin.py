import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("O9g1Ls3wC2E45IsXEyIB5qNzk", "Kt69gbS3NDtSu8D5TIb34XvfgJHpCbPHC4braL4UIKe2oPx717")
auth.set_access_token("1289117209051062272-rxOrDiwY3BuCXthowcnc37ofvOaen9", "FXLZOSU6KtDqE4LH9VO3C8HZ7jz4c8I2escJNAfr2j1YM")

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