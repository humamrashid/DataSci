#!/usr/bin/python3

# Humam Rashid
# CISC 7700X, Prof. Sverdlov

import sys
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

def main():
    dataset = np.loadtxt(open(sys.argv[1], "rb"), delimiter = ",", skiprows = 1, dtype = 'int64')

    # Actual values
    actual = dataset[:, -1].tolist()
    # Assigned values
    assigned = []

    # Confusion matrix
    conf_mat = np.zeros((2, 2), dtype= 'int64')

    # Adjustable intercept
    intercept = int(sys.argv[2])

    # Linear model with zero products removed
    for row in dataset:
        y = (24 * row[0]) + (-15 * row[1]) + (-38 * row[2]) + (-7 * row[3]) + (-41 * row[4]) \
                + (35 * row[5]) + (-2 * row[7]) + (19 * row[8]) + (33 * row[9]) + (-3 * row[10]) \
                + (7 * row[11]) + (3 * row[12]) + (-47 * row[13]) + (26 * row[14]) \
                + (10 * row[15]) + (40 * row[16]) + (-1 * row[17]) + (3 * row[18]) + intercept
        assigned.append(1) if y > 0 else assigned.append(-1)

    # Generate confusion matrix (manual)
    for i, e in enumerate(assigned):
        if actual[i] == 1 and e == 1:
            # True positive
            conf_mat[0, 0] += 1
        elif actual[i] == -1 and e == -1:
            # True negative
            conf_mat[1, 1] += 1
        elif actual[i] == 1 and e == -1:
            # False positive
            conf_mat[0, 1] += 1
        elif actual[i] == -1 and e == 1:
            # False negative
            conf_mat[1, 0] += 1

    # Generate confusion matrix (scikit-learn)
    scikit_mat = confusion_matrix(actual, assigned, labels=[1, -1])
    scikit_report = classification_report(actual, assigned, labels=[1, -1])

    print("1. Confusion matrix (manual):\n")
    print(conf_mat)
    print(f"\nTotal correctly predicted: {conf_mat.diagonal().sum()}\n")
    print("2. Confusion matrix (scikit-learn):\n")
    print(scikit_mat)
    print("\nClassification report (scikit-learn):\n")
    print(scikit_report)

if len(sys.argv) != 3:
    print(f'Usage: {sys.argv[0]} <file_name> <intercept>')
    exit(1)
if __name__ == '__main__':
    main()

# EOF.
