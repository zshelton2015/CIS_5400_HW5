# This sample code is provided by Dr. Fitz to students in CIS5400 at Florida Tech
# to stream tweets using the Twitter streaming API.
# Do not run this code on repl.it

# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
# Use base64 to encode the tweet text to base64 before saving the data to file.
# We do this because the text could contain the delimiters used in
# your CSV file, which could affect reading of the CSV.
import base64

# Variables that contain the user credentials to access Twitter API
ACCESS_TOKEN = "979536259-SFK8LE91RhuITpNGw5x28RykK619mYtfman3dKpG"  # ENTER THE ACCESS TOKEN YOU GET FROM TWITTER HERE
ACCESS_TOKEN_SECRET = "fVeRpGMV2mspuYGljjC2FP3B7f2rMnoubtr3ZoNuKxzbk"  # ENTER YOUR ACCESS TOKEN SECRET HERE
CONSUMER_KEY = "LDIutuhDLa9OGQhXrWT7GZBcZ"  # ENTER YOUR API KEY HERE
CONSUMER_SECRET = "DAT2YPMnc6Kgla6tUcgXPakXqnqPjgptq4oBQqZsnX1v4uDsW0"  # ENTER YOUR API SECRET


# This "class" uses the StreamListener to stream tweets.
# You should only worry about the tweet_store variable and the on_data function.
# The on_data function is called whenever a tweet is streamed.
# The data variable contains a JSON string (data regarding the tweet).
# Use the techniques demonstrated in class to parse the JSON string, 
# extract the information stipulated in the assignment and write the data
# to the tweet_store csv file.

class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to standard output.
    Update this code to extract the data required for the assignment
    """

    # the file handle to a file where you will save the streamed tweets
    tweet_store = open("tweet_store.csv", "w")

    def on_data(self, data):
        print(data)
            # Some tweets may be missing the required keys.
            # As a precaution use try and except to catch the error.
        try:
            # Write code here to process the "data"
            # It is in JSON format.
            # To write to the tweet_store file, use the following line:
            tweet_store.write(data)

            # To encode the text using the base64 library, use:
            text = base64.b64encode(data)
        except AttributeError:
            pass
        return True

    def on_error(self, status):
        print(status)


def main():
    """
    # This handles Twitter authentication and the connection to Twitter Streaming API
    :return:
    """
    listener = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    stream = Stream(auth, listener)

    # This line filters Twitter Streams to capture data by the keywords: 'python', 'pandas', 'data science'
    stream.filter(track=['coronavirus', 'COVID-19', 'SARS-CoV-2', 'novel coronavirus', '2019-nCoV'])

# Invoke the main function to start the program
main()

