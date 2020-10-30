#!/usr/bin/python3

# Humam Rashid
# CISC 7700X, Prof. Sverdlov

import sys
import numpy as np

def main(filename):
    dataset = np.loadtxt(open(filename, "rb"), dtype='float64', delimiter=",")
    print(dataset[-1])

    #actual = dataset[:, -1]
    # Assigned values
    #assigned = []

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <file_name>')
        exit(1)
    main(sys.argv[1])

# EOF.
