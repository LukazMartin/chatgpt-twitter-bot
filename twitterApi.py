import tweepy

class Twitter:

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
    auth.set_access_token("access_token", "access_token_secret")

    # Create API object
    api = tweepy.API(auth)

    # Where On Earth IDentifier
    WOEID = 23424848 # NYC

    def getTrends(self):

        # I am getting only 1 trend because currently chatGPT doesn't allow many requests per month
        trends = self.api.get_place_trends(self.WOEID)[0]['trends'][0]['name'][1:]
        return trends
    
    def postTweet(self, tweet, trend):

        post = tweet + " #" + trend
        status = self.api.update_status(status=tweet)