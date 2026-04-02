from sklearn.feature_extraction.text import TfidfVectorizer

# 5 sample documents
documents = [
    "Machine learning is very useful in data science",
    "Python is widely used for machine learning",
    "Data science involves statistics and programming",
    "Artificial intelligence and machine learning are related",
    "Python programming is important for data analysis"
]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Transform documents
tfidf_matrix = vectorizer.fit_transform(documents)

# Get feature names (words)
features = vectorizer.get_feature_names_out()

print("Top Keywords in Each Document:\n")

for i, doc in enumerate(tfidf_matrix):
    scores = doc.toarray()[0]
    
    # Get top 3 keywords
    top_indices = scores.argsort()[-3:][::-1]
    
    print(f"Document {i+1}:")
    for index in top_indices:
        print(f"{features[index]} ({scores[index]:.2f})")
    print()