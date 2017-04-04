import tweepy

auth = tweepy.OAuthHandler('iV2WBix3Dt8bCWWmQoAToGIA4', 'fSUvPWy0fXfJYG9Jedxb0oGEc6ei6wR5HUs4At44HBIaM3K10Y')
auth.set_access_token('459373640-SlEUk5F12q77C501XpK7EkFY1FO8dNstDfDjCGE8', 'eEDYMrLLVfVOp2KR77fY5PDhVVDeVeG7deV6NdeJSs8eX')

twitter_api = tweepy.API(auth)

tube_game= twitter_api.search(
	q="aaadtubestation"
)
for tweet in tube_game:
	print tweet.user.name + ": " + tweet.text

tube_info= twitter_api.search(
	q="TTfLTravelAlerts"
)
for tweet in tube_info:
	print tweet.user.name + ": " + tweet.text 