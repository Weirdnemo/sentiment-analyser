from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import pandas as pd

class SentimentAnalyzer:
    def __init__(self):
        try:
            nltk.data.find('sentiment/vader_lexicon.zip')
        except LookupError:
            nltk.download('vader_lexicon')
        
        self.sia = SentimentIntensityAnalyzer()

    def analyze_text(self, text):
        scores = self.sia.polarity_scores(text)
        return scores['compound']

    def analyze_messages(self, df):
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame")
        
        df['sentiment'] = df['message'].apply(self.analyze_text)
        return df
