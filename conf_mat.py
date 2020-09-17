#!/usr/bin/python3

# Humam Rashid
# CISC 7700X, Prof. Sverdlov

import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

def main():
    dataset = np.loadtxt(open("hw3.data1.csv", "rb"), delimiter = ",", skiprows = 1)

    # Actual values
    actual = dataset[:, -1]

    print(actual)

if __name__ == '__main__':
    main()

# EOF.
