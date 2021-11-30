from flask import Flask, jsonify
from flask_cors import CORS

from twit import Twit
from storage import Storage

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# creating object of TwitterClient Class
twit_analyzer = Twit()
storage = Storage()

# sanity check route
@app.route('/donald', methods=['GET'])
def don():
    q = 'Donald Trump'
    size = 25
    
    data = handle_query(q, size)
    return jsonify(storage.string_pretty(data))

@app.route('/joe', methods=['GET'])
def joe():
    q = 'Joe Biden'
    size = 25
    
    data = handle_query(q, size)
    return jsonify(storage.string_pretty(data))

@app.route('/elon', methods=['GET'])
def elon():
    q = 'Elon Musk'
    size = 25
    
    data = handle_query(q, size)
    return jsonify(storage.string_pretty(data))

def handle_query(q, size):
    # DO ANALYSIS
    tweets, avg_polarity, avg_rounded_polarity = twit_analyzer.get_tweets(query=q, count=size)
    
    # SAVE IT ALL
    data = storage.format_json(tweets, avg_polarity, avg_rounded_polarity, q, size)
    storage.save_run(data)
    
    return data
    


if __name__ == '__main__':
    app.run()