import random
import pandas as pd
from datetime import datetime, timedelta

class MockDataGenerator:
    def __init__(self):
        self.messages = [
            "This hackathon is awesome! 🚀",
            "Stuck with this bug for hours 😫",
            "Finally fixed the issue!",
            "Need help with the API",
            "Great progress on our project",
            "Running into some problems",
            "Team meeting went well",
            "Getting tired...",
            "Just had a breakthrough!",
            "Coffee break time ☕",
        ]
        self.users = ["User" + str(i) for i in range(1, 6)]

    def generate_message(self, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now()
        
        return {
            'timestamp': timestamp,
            'user': random.choice(self.users),
            'message': random.choice(self.messages)
        }

    def generate_batch(self, n_messages=10, time_range_minutes=30):
        current_time = datetime.now()
        messages = []
        
        for _ in range(n_messages):
            random_minutes = random.uniform(0, time_range_minutes)
            timestamp = current_time - timedelta(minutes=random_minutes)
            messages.append(self.generate_message(timestamp))
        
        return pd.DataFrame(messages).sort_values('timestamp')
