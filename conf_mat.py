#!/usr/bin/python3

# Humam Rashid
# CISC 7700X, Prof. Sverdlov

import sys
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

def main(filename, intercept):
    dataset = np.loadtxt(open(filename, "rb"), delimiter = ",", skiprows = 1, dtype = 'int32')

    # Actual values
    actual = dataset[:, -1].tolist()
    # Assigned values
    assigned = []

    # Confusion matrix
    conf_mat = np.zeros((2, 2), dtype = 'int32')
    # Economic gain matrix
    econ_mat = np.zeros((2, 2), dtype = 'int32')

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

    TP = conf_mat[0, 0]
    TN = conf_mat[1, 1]
    FP = conf_mat[0, 1]
    FN = conf_mat[1, 0]

    accuracy = (TP + TN) / (TP + TN + FP + FN)

    # Generate confusion matrix with scikit-learn for verification
    scikit_mat = confusion_matrix(actual, assigned, labels = [1, -1])
    scikit_report = classification_report(actual, assigned, labels = [1, -1])

    print("1. Confusion matrix (manual):\n\n", conf_mat)
    print("\nAccuracy: ", accuracy, end = "\n\n")
    print("2. Confusion matrix (scikit-learn):\n\n", scikit_mat)
    print("\nClassification report (scikit-learn):\n\n", scikit_report)
    print("Economic gain: ", round((accuracy * 0) + ((1.00 - accuracy) * (100 + 1000)), 2))

if len(sys.argv) != 3:
    print(f'Usage: {sys.argv[0]} <file_name> <intercept>')
    exit(1)
if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))

# EOF.
