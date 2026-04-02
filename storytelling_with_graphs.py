import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Student': ['Asha', 'Rahul', 'Meena', 'Arjun', 'Priya'],
    'Math': [85, 78, 92, 70, 95],
    'Science': [78, 82, 89, 65, 91],
    'English': [90, 76, 95, 80, 88]
}

df = pd.DataFrame(data)

# ---------- Bar Chart ----------
plt.figure()
plt.bar(df['Student'], df['Math'])
plt.title("Math Scores of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# ---------- Pie Chart ----------
plt.figure()
plt.pie(df['Math'], labels=df['Student'], autopct='%1.1f%%')
plt.title("Distribution of Math Marks")
plt.show()

# ---------- Histogram ----------
plt.figure()
plt.hist(df['Math'], bins=5)
plt.title("Histogram of Math Scores")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()