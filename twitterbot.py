import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("Xeic6A6QkhDG4AQnvjVIJJ37J", "VP54jcIt5uCNJEHHqQUme8KN0Kmgprdtl5b5wlkvPujgETGfwY")
auth.set_access_token("1289117209051062272-udu9y5BYw8GNeGLqRuHcCuFodjrksQ", "Iop2nctZq6UcLKSw0SiLYChZl4vXAYSmvUrA7GOw9WrmO")

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
