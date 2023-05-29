# Twitter Data Scraper

This project is a Python script that utilizes the Tweepy library to scrape tweets from Twitter based on specific parameters, such as hashtags, date range, and optional location. The scraped tweets are saved to a CSV file for further analysis.

## Prerequisites

- Python 3.x
- Tweepy library: Install it by running `pip install tweepy`

## Getting Started


1. Create a Twitter Developer account and obtain API credentials (consumer key, consumer secret, access token, and access token secret). Make sure you have read access to the Twitter API.

2. Create a file named `credentials.txt` in the project directory and place your Twitter API credentials inside it in the format:
consumer_key=YOUR_CONSUMER_KEY
consumer_secret=YOUR_CONSUMER_SECRET
access_token=YOUR_ACCESS_TOKEN
access_token_secret=YOUR_ACCESS_TOKEN_SECRET


3. Modify the script parameters in the `scrape_tweets` function within the `twitter_data_scraper.py` file. Update the hashtags, date range, and location as per your requirements.

4. Run the script: python twitter_data_scraper.py


5. The scraped tweets will be saved to a CSV file named `scraped_tweets.csv` in the project directory.

## Customization

- You can modify the script to perform additional processing on the scraped tweets or store them in a different format.
- Feel free to adjust the search parameters, such as hashtags, date range, and location, based on your needs.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

Please be aware of Twitter's terms of service and API usage policy. Ensure that your usage of the Twitter API is compliant with



