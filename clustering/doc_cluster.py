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

def assign_cat(km, max_feat, doc_path):
    doc = []
    with open(doc_path, errors='ignore') as text_input:
        doc.append(text_input.read())
    vectorizer = TfidfVectorizer(max_features=max_feat, stop_words='english')
    vector = extract_features(vectorizer, doc)
    return km.predict(vector)

def ask_docs(km, max_feat):
    while True:
        print('\nEnter new document to categorize:', end=' ')
        doc_path = input()
        if len(doc_path) == 0:
            break
        print(f'Assigning category to new document: {doc_path}...')
        cat = assign_cat(km, max_feat, doc_path)
        print(f'New document belongs to category: {cat[0]}')

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
    km.fit(vector)

def extract_features(vectorizer, text_data):
    vector = vectorizer.fit_transform(text_data)
    x, y = vector.shape
    print(f'Number of documents: {x}\nNumber of features: {y}')
    return vector

def get_corpus(dirname, ext):
    corpus = []
    all_files = glob.glob(os.path.join(os.getcwd(), dirname, '*.' + ext))
    for path in all_files:
        with open(path, errors='ignore') as text_input:
            corpus.append(text_input.read())
    return corpus

def main(dirname, ext, K, new_doc, iters, max_feat):
    print('Loading data...', end='')
    corpus = get_corpus(dirname, ext)
    print(f'corpus size: {len(corpus)} documents')
    print(f"Extracting features from training dataset...")
    start = time()
    vectorizer = TfidfVectorizer(min_df=0.05, max_df=0.95, \
            max_features=max_feat, stop_words='english')
    vector = extract_features(vectorizer, corpus)
    print(f'Clustering data with K={K}...')
    km = KMeans(n_clusters=K, init='random', max_iter=iters, n_init=1, \
            verbose=True)
    cluster_kmeans(km, vector, K)
    print()
    show_clusters(vectorizer, km, K)
    if new_doc.lower() == "yes":
        ask_docs(km, max_feat)
    print(f'\nOverall elapsed time: {time() - start}s')

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 6 or argc > 7:
        print(f'Usage: {sys.argv[0]} <train_dir> <file_ext> <K>' \
                ' <new_doc?> <max_iter> [max_features]')
        exit(1)
    if argc == 6:
        main(sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], \
                int(sys.argv[5]), None)
    else:
        main(sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], \
                int(sys.argv[5]), int(sys.argv[6]))

# EOF.
