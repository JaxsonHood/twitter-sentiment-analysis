from flask import Flask, jsonify
from flask_cors import CORS
from twit import Twit

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# creating object of TwitterClient Class
client = Twit()

# sanity check route
@app.route('/donald', methods=['GET'])
def don():
    # Replace with your own search query
    q = 'Donald Trump'
    size = 10
    tweets, avg_polarity, avg_rounded_polarity = client.get_tweets(query=q, count=size)
    return jsonify("Query={}, Avg Polarity={}, Avg Rounded Polarity={}, Sample Size={}".format(q, avg_polarity, avg_rounded_polarity, size))

@app.route('/joe', methods=['GET'])
def joe():
    # Replace with your own search query
    q = 'Joe Biden'
    size = 10
    tweets, avg_polarity, avg_rounded_polarity = client.get_tweets(query=q, count=size)
    return jsonify("Query={}, Avg Polarity={}, Avg Rounded Polarity={}, Sample Size={}".format(q, avg_polarity, avg_rounded_polarity, size))


if __name__ == '__main__':
    app.run()