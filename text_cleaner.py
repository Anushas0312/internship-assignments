import string

# Simple stopwords list
stopwords = ["is", "am", "are", "the", "a", "an", "and", "or", "in", "on", "at", "to"]

# Input text
text = input("Enter a sentence: ")

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))

# Remove stopwords
words = text.split()
cleaned_words = [word for word in words if word not in stopwords]

cleaned_text = " ".join(cleaned_words)

print("\nCleaned Text:")
print(cleaned_text)