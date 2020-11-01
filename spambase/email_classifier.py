#!/usr/bin/python3

# Humam Rashid
# CISC 7700X, Prof. Sverdlov

import sys
import numpy as np

def exit_err(msg, err):
    print(msg, file=sys.stderr)
    sys.exit(err)

def get_prior(dataset, num_inst, label_pos):
    prior = {}
    count_spam = 0
    count_ham = 0
    for i in range(num_inst):
        if dataset[i][label_pos - 1] == 1.0:
            count_spam += 1
        else:
            count_ham += 1

    prior['spam'] = count_spam / num_inst
    prior['ham'] = count_ham / num_inst
    return prior

def get_attrtable(dataset, num_inst, num_attrs, label_pos):
    table = {}
    table['spam'] = np.empty(num_attrs, dtype='float64')
    table['ham'] = np.empty(num_attrs, dtype='float64')
    occ_total = np.zeros(num_attrs, dtype='int64')
    occ_spam = np.zeros(num_attrs, dtype='int64')
    occ_ham = np.zeros(num_attrs, dtype='int64')
    for i in range(num_inst):
        for j in range(num_attrs):
            if dataset[i][j] != 0.0:
                # Word occurs
                occ_total[j] += 1
                if dataset[i][label_pos - 1] == 1.0:
                    # Word is spam
                    occ_spam[j] += 1
                elif dataset[i][label_pos - 1] == 0.0:
                    # Word is not spam
                    occ_ham[j] += 1
    for k in range(num_attrs):
        if occ_total[k] != 0:
            table['spam'][k] = occ_spam[k] / occ_total[k]
            table['ham'][k] = occ_ham[k] / occ_total[k]
        else:
            table['spam'][k] = 0.0
            table['ham'][k] = 0.0
    return table

def main(filename, num_inst, num_attrs, label_pos):
    dataset = np.loadtxt(open(filename, "rb"), dtype='float64', delimiter=",")
    # prior[spam|ham]
    prior = get_prior(dataset, num_inst, label_pos)
    # table[spam|ham][word]
    table = get_attrtable(dataset, num_inst, num_attrs, label_pos)

if __name__ == '__main__':
    if len(sys.argv) != 5:
        exit_err(f'Usage: {sys.argv[0]} <file_name> <num_inst> <num_attrs>' \
                + ' <label_pos>', 1)
    num_inst = int(sys.argv[2])
    if num_inst <= 0:
        exit_err('Number of instances must be > 0', 1)
    num_attrs = int(sys.argv[3])
    if num_attrs <= 0:
        exit_err('Number of words must be > 0', 1)
    label_pos = int(sys.argv[4])
    if label_pos < 0:
        exit_err('Label position must be >= 0', 1)
    main(sys.argv[1], num_inst, num_attrs, label_pos)

# EOF.
