from flask import Flask, jsonify, request
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
@app.route('/analyse', methods=['POST'])
def analyse():
    data = request.get_json()
    q = data['query']
    size = 100
    
    return handle_query(q, size)


@app.route('/saved', methods=['GET'])
def saved():
    return storage.read_saved()

@app.route('/find', methods=['POST'])
def find():
    data = request.get_json()
    timestamp = data['timestamp']
    return storage.find_tweets(timestamp)

def handle_query(q, sample_size):
    # DO ANALYSIS
    tweets, avg_polarity, avg_rounded_polarity, actual_size = twit_analyzer.get_tweets(query=q, count=sample_size)
    
    if (actual_size < 1):
        return {'data': []}
    else:
        # SAVE IT ALL
        data = storage.format_json(tweets, avg_polarity, avg_rounded_polarity, q, actual_size)
        storage.save_run(data)
        return data
    


if __name__ == '__main__':
    app.run()