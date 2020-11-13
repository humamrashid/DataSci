#!/usr/bin/python3

# Document clustering.
# Humam Rashid
# CISC 7700X, Prof. Sverdlov

import math
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Return the Euclidean distance between a and b.
def calc_dist(a, b):
    s = 0
    for e in list(zip(a, b)):
        s += (e[0] - e[1])**2
    return math.sqrt(s)

def count_vec(text):
    vectorizer = CountVectorizer()
    vectorizer.fit(text)
    print(vectorizer.vocabulary_)
    vector = vectorizer.transform(text)
    print(vector.shape)
    print(type(vector))
    print(vector.toarray())

def tfidf_vec(text):
    vectorizer = TfidfVectorizer()
    vectorizer.fit(text)
    print(vectorizer.vocabulary_)
    print(vectorizer.idf_)
    vector = vectorizer.transform([text[0]])
    print(vector.shape)
    print(vector.toarray())

def main():
    text = ["The quick brown fox jumped over the lazy dog.",
            "the dog",
            "the fox"]
    tfidf_vec(text)

if __name__ == "__main__":
    main()

# EOF.
