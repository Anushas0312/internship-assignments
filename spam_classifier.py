from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training dataset
messages = [
    "Win a free lottery now",
    "Congratulations you won money",
    "Hello how are you",
    "Let's meet tomorrow",
    "Claim your free prize now",
    "Are we still meeting today"
]

labels = ["spam", "spam", "ham", "ham", "spam", "ham"]

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Test message
new_message = ["Win free cash prize"]

X_test = vectorizer.transform(new_message)

prediction = model.predict(X_test)

print("Message:", new_message[0])
print("Prediction:", prediction[0])