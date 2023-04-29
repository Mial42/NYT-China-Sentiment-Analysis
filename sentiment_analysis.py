import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

df = pd.read_csv('china_articles.csv')
# print(len(df))
# df = df[df['year'].astype(str).str.isdigit()]

# # Save the updated DataFrame to a CSV file or do further analysis
# df.to_csv('china_articles_cleaned.csv', index=False)
# print(len(df))

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

def get_sentiment(text):
    global sid
    blob = TextBlob(text)
    scores = sid.polarity_scores(text)
    nltk_score = scores['compound']
    return (blob.sentiment.polarity, blob.sentiment.subjectivity, nltk_score)
    

# Apply the get_sentiment function to each row of the DataFrame and add the results as new columns
df[['TextBlob_sentiment', 'TextBlob_subjectivity', 'NLTK_sentiment']] = df['article'].apply(lambda x: pd.Series(get_sentiment(x)))
df.to_csv('china_articles_analyzed.csv', index=False)