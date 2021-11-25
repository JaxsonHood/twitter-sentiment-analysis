from flask import Flask, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/dong', methods=['GET'])
def pong_dong():
    return jsonify('pong dong!')


if __name__ == '__main__':
    app.run()