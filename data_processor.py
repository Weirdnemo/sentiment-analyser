import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self, window_size=5):
        self.window_size = window_size
        self.data = pd.DataFrame()

    def update_data(self, new_data):
        self.data = pd.concat([self.data, new_data], ignore_index=True)
        self.data = self.data.sort_values('timestamp')
        
        # Keep only last hour of data
        one_hour_ago = pd.Timestamp.now() - pd.Timedelta(hours=1)
        self.data = self.data[self.data['timestamp'] > one_hour_ago]

    def get_rolling_sentiment(self):
        return self.data['sentiment'].rolling(window=self.window_size).mean()

    def get_current_mood(self):
        if len(self.data) == 0:
            return "Neutral", 0
        
        recent_sentiment = self.data['sentiment'].iloc[-self.window_size:].mean()
        
        if recent_sentiment >= 0.5:
            mood = "Very Positive"
        elif recent_sentiment >= 0.1:
            mood = "Positive"
        elif recent_sentiment >= -0.1:
            mood = "Neutral"
        elif recent_sentiment >= -0.5:
            mood = "Negative"
        else:
            mood = "Very Negative"
            
        return mood, recent_sentiment

    def get_stats(self):
        if len(self.data) == 0:
            return {
                "message_count": 0,
                "avg_sentiment": 0,
                "positive_ratio": 0,
                "negative_ratio": 0
            }
            
        stats = {
            "message_count": len(self.data),
            "avg_sentiment": self.data['sentiment'].mean(),
            "positive_ratio": (self.data['sentiment'] > 0).mean() * 100,
            "negative_ratio": (self.data['sentiment'] < 0).mean() * 100
        }
        return stats
