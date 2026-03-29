import nltk
import random
import string

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

stemmer = PorterStemmer()

# Load training data
questions = []
answers = []

with open("training_data.txt", "r") as file:
    for line in file:
        if "|" in line:
            q, a = line.strip().split("|", 1)
            questions.append(q.lower())
            answers.append(a)

# Text preprocessing
def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [stemmer.stem(word) for word in tokens if word not in stopwords.words('english')]
    return tokens

# Similarity checking
def similarity(user_input):
    user_tokens = preprocess(user_input)
    scores = []

    for q in questions:
        q_tokens = preprocess(q)

        match = len(set(user_tokens) & set(q_tokens))
        scores.append(match)

    best_match = scores.index(max(scores))

    if max(scores) == 0:
        return "Sorry, I don't understand that yet."

    return answers[best_match]

print("AI Chatbot (Type 'bye' to exit)")
print("--------------------------------")

while True:

    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break

    response = similarity(user_input)

    print("Bot:", response)
