import tweepy
from time import sleep
from Grumba_bot import Grumba

# Function to sleep for a set number of minutes
def sleep_min(minutes):
        sleep(minutes*60)

# # Authentication data for twitter
# auth = tweepy.OAuthHandler("Z6DJoiHjExjTiBh7eBSu976xd", "WWooaalC3TY1E06o52waBrQI8QQVtDyhp9bW0wNEysMJ8H4ePh")
# auth.set_access_token("2757554222-IbgaNw2WZmEQAyDuvp3LnLLfyrseXX86ksMbzxc", "T7o6tYB7ALGYHyk1OZkewKKYEZcI29a6RKPd0LVyrNdlb")

# # Set up API variable
# api = tweepy.API(auth)

# # Get User object of dedicated user
# rico = api.get_user(screen_name="ErynTheFool")
# # Get list of most recent tweets that are not replies or retweets 
# r_timeline = api.user_timeline(user_id=rico.id, count=10, exclude_replies=True, include_rts=False, tweet_mode="extended")

# newest_tweet = r_timeline[0]


# media = api.media_upload("./images/Dr_Phil_M.png")
# tweet_txt = "Candace?"

# # Respond to newest tweet of user
# post_result = api.update_status(status=tweet_txt, in_reply_to_status_id=newest_tweet.id, auto_populate_reply_metadata=True, media_ids=[media.media_id])

bot = Grumba("GrumbaBot")

while(True):
        sleep_min(5)
        bot.respond()
  


