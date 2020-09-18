#!/usr/bin/python3

# Humam Rashid
# CISC 7700X, Prof. Sverdlov

import sys
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

def main():
    dataset = np.loadtxt(open("hw3.data1.csv", "rb"), delimiter = ",", skiprows = 1, dtype='int8')

    # Actual values
    actual = dataset[:, -1]
    # Assigned values
    assigned = []

    for row in dataset:
        y = (24 * row[0]) + (-15 * row[1]) + (-38 * row[2]) + (-7 * row[3]) + (-41 * row[4]) \
                + (35 * row[5]) + (0 * row[6]) + (-2 * row[7]) + (19 * row[8]) + (33 * row[9]) \
                + (-3 * row[10]) + (7 * row[11]) + (3 * row[12]) + (-47 * row[13]) \
                + (26 * row[14]) + (10 * row[15]) + (40 * row[16]) + (-1 * row[17]) \
                + (3 * row[18]) + (0 * row[19]) + (-6)
        assigned.append(1) if y > 0 else assigned.append(-1)

    print(len(actual))
    print(len(assigned))

if __name__ == '__main__':
    main()

# EOF.
