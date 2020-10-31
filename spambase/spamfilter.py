#!/usr/bin/python3

# Humam Rashid
# CISC 7700X, Prof. Sverdlov

import sys
import numpy as np

POS_CLASS = 58

def main(filename):
    dataset = np.loadtxt(open(filename, "rb"), dtype='float64', delimiter=",")
    num_rows, num_cols = dataset.shape
    
    # Fraction of emails of category spam
    count_spam = 0
    count_ham = 0
    p_spam = 0
    for i in range(num_rows):
        if dataset[i][POS_CLASS -1] == 1.0:
            count_spam += 1
        else:
            count_ham += 1
    print("Spam count=", count_spam)
    print("Ham count=", count_ham)

    table = {}

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <file_name>')
        exit(1)
    main(sys.argv[1])

# EOF.
