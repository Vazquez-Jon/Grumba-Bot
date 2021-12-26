# Class of Person and their data

class Person:
    def __init__(this, bot, username) -> None:
        this.bot = bot
        this.user = bot.getUser(username)
        tweets = bot.user_timeline(user_id=this.user.id, count=10, exclude_replies=True, include_rts=False, tweet_mode="extended")
        this.newest_status = tweets[0]

    def new_post(this, media_file, tweet_txt):
        tmp_tweet = this.bot.user_timeline(user_id=this.user.id, count=10, exclude_replies=True, include_rts=False, tweet_mode="extended")[0]
        # If there's a new tweet
        if( this.newest_status.id !=  tmp_tweet.id):
            # Update the newest tweet
            this.newest_status = tmp_tweet
            # Post the response
            media = this.bot.media_upload("../images/" + media_file)
            this.bot.update_status(status=tweet_txt, in_reply_to_status_id=this.newest_status.id, auto_populate_reply_metadata=True, media_ids=[media.media_id])

    # TO DO make it so once people are created, will respond once(the "first" response)
