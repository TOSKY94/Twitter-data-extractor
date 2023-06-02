import tweepy
import csv
import datetime

# Load Twitter API credentials from a separate file
def load_credentials(file_path):
    credentials = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            credentials[key] = value
    return credentials

# Authenticate to Twitter
def authenticate_twitter_api(credentials):
    auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
    auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])
    return tweepy.API(auth)

# Function to scrape tweets based on parameters
def scrape_tweets(api, keywords, start_date, end_date, location):
    tweets = []
    query = ' '.join(keywords)
    if location:
        query += f' near:"{location}"'

    # Scrape tweets within the date range
    for tweet in tweepy.Cursor(api.search, q=query, lang='en', tweet_mode='extended').items():
        if tweet.created_at < start_date:
            # Reached tweets before the start date, stop scraping
            return tweets

        if tweet.created_at <= end_date:
            # Add tweet to the list
            tweets.append(tweet._json)
        else:
            # Move on to the next keyword
            break

    return tweets


# Save tweets to a CSV file
def save_tweets_to_csv(tweets, file_path):
    keys = tweets[0].keys() if tweets else []
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(tweets)

# Example usage
keywords = ['example1', 'example2']  # List of hashtags to search for
start_date = datetime.datetime(2023, 5, 1, 0, 0, 0)  # Start date of the date range
end_date = datetime.datetime(2023, 5, 15, 0, 0, 0)  # End date of the date range
location = 'New York City'  # Location to search near (optional)

# Load API credentials from file
credentials = load_credentials('credentials.txt')

# Authenticate to Twitter API
api = authenticate_twitter_api(credentials)

# Scrape tweets
scraped_tweets = scrape_tweets(api, keywords, start_date, end_date, location)

# Save tweets to a CSV file
save_tweets_to_csv(scraped_tweets, 'scraped_tweets.csv')
