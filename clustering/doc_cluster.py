#!/usr/bin/python3

# Document clustering.
# Humam Rashid
# CISC 7700X, Prof. Sverdlov

import os
import sys
import glob
from time import time
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

def assign_cat(km, doc_path):
    doc = []
    with open(doc_path, errors='ignore') as text_input:
        doc.append(text_input.read())
    #km.predict(doc)

def show_clusters(vectorizer, km, K):
    terms = vectorizer.get_feature_names()
    order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    print('Top terms per cluster:')
    for i in range(K):
        print(f'Cluster {i}:', end='')
        for j in order_centroids[i, :10]:
            print(f' {terms[j]}', end='')
        print()

def cluster_kmeans(km, vector, K):
    start = time()
    km.fit(vector)
    print(f'Clustering elapsed time: {time() - start}s')

def extract_features(vectorizer, corpus):
    start = time()
    vector = vectorizer.fit_transform(corpus)
    print(f'Feature extraction elapsed time: {time() - start}s')
    x, y = vector.shape
    print(f'Number of samples: {x}\nNumber of features: {y}')
    return vector

def get_corpus(dirname, ext):
    corpus = []
    all_files = glob.glob(os.path.join(os.getcwd(), dirname, '*.' + ext))
    for path in all_files:
        with open(path, errors='ignore') as text_input:
            corpus.append(text_input.read())
    return corpus

def main(dirname, ext, K, new_doc, max_feat):
    print('Loading data...', end='')
    corpus = get_corpus(dirname, ext)
    print(f'corpus size: {len(corpus)} files')
    print(f"Extracting features from training dataset...")
    start = time()
    vectorizer = TfidfVectorizer(min_df=2, max_df=0.5, max_features=max_feat, \
            stop_words='english')
    vector = extract_features(vectorizer, corpus)
    print(f'Clustering data with K={K}...')
    km = KMeans(n_clusters=K, init='random', max_iter=100, n_init=1, \
            verbose=True)
    cluster_kmeans(km, vector, K)
    print(f'Overall elapsed time: {time() - start}s')
    print()
    show_clusters(vectorizer, km, K)
    print('Assigning category to new document: {new_doc}...')
    assign_cat(km, new_doc)

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 5 or argc > 6:
        print(f'Usage: {sys.argv[0]} <train_dir> <file_ext> <K>' \
                ' <new_doc> [max_features]')
        exit(1)
    if argc == 5:
        main(sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], None)
    else:
        main(sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], \
                int(sys.argv[5]))

# EOF.
