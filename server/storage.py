from datetime import datetime
import json

class Storage(object):
    def __init__(self):
        self.filename = "saved_data.json"

    def save_run(self, data):
        # Get saved data
        saved = self.read_saved()
        saved["data"].append(data)
        
        json_object = json.dumps(saved, indent = 4)
        
        with open(self.filename, "w") as outfile:
            outfile.write(json_object)
        
            
    def read_saved(self):
        with open(self.filename, 'r') as openfile:
            json_object = json.load(openfile)
            return json_object
        
    def find_tweets(self, timestamp):
        data = self.read_saved()
        
        for item in data['data']:
            if (item['timestamp'] == timestamp):
                return item
            
        
    def format_json(self, tweets, avg_score, overall_sentiment, q, size):
        now = datetime.today()
        
        return {
            "tweets": tweets,
            "avg_score": avg_score,
            "overall_sentiment": overall_sentiment,
            "query": q,
            "size": size,
            "timestamp": str(now)
        }
    
    def string_pretty(self, data):
        return "Query={}, Avg Polarity={}, Avg Rounded Polarity={}, Sample Size={}, Timestamp={}".format(data["query"], data["avg_polarity"], data["avg_rounded_polarity"], data["size"], data["timestamp"])
    
  