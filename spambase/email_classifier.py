#!/usr/bin/python3

# Humam Rashid
# CISC 7700X, Prof. Sverdlov

import sys
import numpy as np

def exit_err(msg, err):
    print(msg, file=sys.stderr)
    sys.exit(err)

def get_pcat(dataset, num_inst, label_pos):
    count_spam = 0
    count_ham = 0
    for i in range(num_inst):
        if dataset[i][label_pos - 1] == 1.0:
            count_spam += 1
        else:
            count_ham += 1
    return (count_spam / num_inst, count_ham / num_inst)

def get_pwordinclass(dataset, num_inst, num_words, label_pos):
    table = {}
    table['spam'] = np.zeros(num_words, dtype='float64')
    table['ham'] = np.zeros(num_words, dtype='float64')
    occ_total = np.zeros(num_words, dtype='int64')
    occ_spam = np.zeros(num_words, dtype='int64')
    occ_ham = np.zeros(num_words, dtype='int64')
    for i in range(num_inst):
        for j in range(num_words):
            if dataset[i][j] != 0.0:
                # Word occurs
                occ_total[j] += 1
                if dataset[i][label_pos - 1] == 1.0:
                    # Word is spam
                    occ_spam[j] += 1
                elif dataset[i][label_pos - 1] == 0.0:
                    # Word is not spam
                    occ_ham[j] += 1
    print("Occ_total:", occ_total)
    print("Occ_spam:", occ_spam)
    print("Occ_ham:", occ_ham)
    for k in range(num_words):
        if occ_total[k] != 0:
            table['spam'][k] = occ_spam[k] / occ_total[k]
            table['ham'][k] = occ_ham[k] / occ_total[k]
        else:
            table['spam'][k] = 0.0
            table['ham'][k] = 0.0
    print("spam probs:", table['spam'])
    print("ham probs:", table['ham'])
    return table

def main(filename, num_inst, num_words, label_pos):
    dataset = np.loadtxt(open(filename, "rb"), dtype='float64', delimiter=",")
    
    # p(spam), p(ham)
    p_spam, p_ham = get_pcat(dataset, num_inst, label_pos)

    # p(word_in_class)
    table = get_pwordinclass(dataset, num_inst, num_words, label_pos)

if __name__ == '__main__':
    if len(sys.argv) != 5:
        exit_err(f'Usage: {sys.argv[0]} <file_name> <num_inst> <num_words>' \
                + ' <label_pos>', 1)
    num_inst = int(sys.argv[2])
    if num_inst <= 0:
        exit_err('Number of instances must be > 0', 1)
    num_words = int(sys.argv[3])
    if num_words <= 0:
        exit_err('Number of words must be > 0', 1)
    label_pos = int(sys.argv[4])
    if label_pos < 0:
        exit_err('Label position must be >= 0', 1)
    main(sys.argv[1], num_inst, num_words), label_pos)

# EOF.
