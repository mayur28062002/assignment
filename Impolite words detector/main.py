import re

def calculate_rudeness(sentence, bad_words):
    sentence = sentence.lower()
    words = re.findall(r'\w+', sentence)
    num_bad_words = sum(word in bad_words for word in words)
    return num_bad_words / len(words) if len(words) > 0 else 0

def analyze_tweets(file_path, bad_words):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            sentence = line.strip()
            degree = calculate_rudeness(sentence, bad_words)
            print(f"Sentence: {sentence}")
            print(f"Degree of Rudeness: {degree}")
            print()

# Replace with your set of impolite words
bad_words = {'stupid', 'fool', 'idiot'}

# Replace with the path to your file containing the tweets
file_path = 'tweets.txt'

analyze_tweets(file_path, bad_words)
