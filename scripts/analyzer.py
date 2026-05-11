from textblob import TextBlob
import pandas as pd

class FinancialAnalyzer:
    @staticmethod
    def get_sentiment(text):
        """
        Task 2: NLP Sentiment Analysis.
        Returns a score from -1 (Negative) to 1 (Positive).
        """
        if pd.isna(text) or text == "":
            return 0.0
        # This calculates the 'vibe' of the headline
        return TextBlob(str(text)).sentiment.polarity

    @staticmethod
    def categorize_sentiment(score):
        """
        Categorizes scores for the report visualizations.
        """
        if score > 0.1:
            return 'Positive'
        elif score < -0.1:
            return 'Negative'
        else:
            return 'Neutral'