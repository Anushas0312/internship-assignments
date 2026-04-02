from textblob import TextBlob

# 5 sample movie reviews
reviews = [
    "The movie was amazing and very entertaining",
    "I did not like the film, it was boring",
    "The acting was good but the story was average",
    "Absolutely fantastic movie, I loved it",
    "The movie was terrible and waste of time"
]

print("Sentiment Analysis Results:\n")

for review in reviews:
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print("Review:", review)
    print("Sentiment:", sentiment)
    print()