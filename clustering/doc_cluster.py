#!/usr/bin/python3

# Document clustering.
# Humam Rashid
# CISC 7700X, Prof. Sverdlov

import os
import sys
import glob
import numpy as np
from time import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import KMeans

def get_corpus(dirname, ext):
    corpus = []
    all_files = glob.glob(os.path.join(os.getcwd(), dirname, '*.' + ext))
    for path in all_files:
        with open(path, errors='ignore') as text_input:
            corpus.append(text_input.read())
    return corpus

def main(dirname, ext):
    categories = None
    corpus = get_corpus('temp', ext)
    print(f'Corpus size: {len(corpus)}')
    start =  time()
    vectorizer = TfidfVectorizer(min_df=2, max_df=0.5, stop_words='english')
    #vectorizer.fit(corpus)
    #vector = vectorizer.transform(corpus)
    #print(vectorizer.vocabulary_)
    vector = vectorizer.fit_transform(corpus)
    x, y = vector.shape
    print(f'Elapsed time: {time() - start}s')
    print(f'No. of samples: {x}\nNo. of features: {y}')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} <files_dir> <file_ext>')
        exit(1)
    main(sys.argv[1], sys.argv[2])

# EOF.
