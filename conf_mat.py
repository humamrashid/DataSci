#!/usr/bin/python3

# Humam Rashid
# CISC 7700X, Prof. Sverdlov

import csv
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

filename = "hw3.data1.csv"

fields = []
rows = []
actual = []

def main():
    dataset = np.loadtxt(open("hw3.data1.csv", "rb"), delimiter=",", skiprows=1)
    print((dataset[:,-1]))

if __name__ == '__main__':
    main()

# EOF.
