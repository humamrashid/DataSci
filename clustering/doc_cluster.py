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
    #vectorizer.fit(corpus)
    #vector = vectorizer.transform(corpus)
    #print(vectorizer.vocabulary_)

def main(dirname, ext, K):
    categories = None
    corpus = get_corpus('temp', ext)
    print(f'Corpus size: {len(corpus)}')
    print(f"Extracting features from training dataset: {dirname}{'*.' + ext}")
    overall_t = part_t =  time()
    vectorizer = TfidfVectorizer(min_df=2, max_df=0.5, stop_words='english')
    vector = vectorizer.fit_transform(corpus)
    print(f'Feature extraction elapsed time: {time() - part_t}s')
    x, y = vector.shape
    print(f'No. of samples: {x}\nNo. of features: {y}')
    km = KMeans(n_clusters=K, init='random', max_iter=100, n_init=1, verbose=1)
    print(f'Clustering data with {km}')
    part_t = time()
    km.fit(vector)
    print(f'Clustering elapsed time: {time() - part_t}s')
    print(f'Overall elapsed time: {time() - overall_t}s')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f'Usage: {sys.argv[0]} <files_dir> <file_ext> <K>')
        exit(1)
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]))

# EOF.
