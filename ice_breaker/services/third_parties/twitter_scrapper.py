from configurations.settings import settings
import tweepy

class TwitterScraper:
    """A class to fetch tweets from Twitter using the Tweepy API."""
    
    def __init__(self):
        """Initializes the TwitterScraper with credentials and sets up API access."""
        self.consumer_key = settings.CONSUMER_KEY
        self.consumer_secret = settings.CONSUMER_SECRET
        self.access_token = settings.ACCESS_TOKEN
        self.access_token_secret = settings.ACCESS_TOKEN_SECRET

        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)

    def fetch_tweets(self, twitter_handle: str) -> str:
        """
        Fetches and returns tweets for a specified Twitter handle.
        
        Parameters:
            twitter_handle (str): The Twitter handle for which to fetch tweets.
        
        Returns:
            str: A string containing the fetched tweets or an error/message.
        """
        try:
            tweets = self.api.user_timeline(screen_name=twitter_handle, count=5)
            if tweets:
                return ' '.join(tweet.text for tweet in tweets)
            else:
                return (f"Due to the new Twitter CEO policies, it is more restricted "
                        f"to find user information. We can only say that the Twitter user is {twitter_handle}.")

        except tweepy.Forbidden:
            return (f"Due to the new Twitter CEO policies, it is more restricted "
                    f"to find user information. We can only say that the Twitter user is {twitter_handle}.")
        except tweepy.TweepError as e:
            return (f"Failed to retrieve tweets due to an error: {e}. "
                    F"We can only say that the Twitter user is {twitter_handle}.")
