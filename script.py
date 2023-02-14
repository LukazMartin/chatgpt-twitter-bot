from openaiApi import OpenAI
from twitterApi import Twitter
import datetime

# Authentification to Twitter
twitter = Twitter()

# Get most trending #
trends = twitter.getTrends()

# Call chatGPT with the prompt
prompt = f'Write a short funny tweet about {trends}'
response = OpenAI(prompt)

# Saving a copy file
with open(datetime.now().strftime("%Y%m%d-%H%M%S"),"w") as file:
    file.write(response)

# Post the tweet
twitter.postTweet(response, trends)
