#!/usr/bin/python3

# Document clustering.
# Humam Rashid
# CISC 7700X, Prof. Sverdlov

import math

# Return the Euclidean distance between a and b.
def calc_dist(a, b):
    s = 0
    for e in list(zip(a, b)):
        s += (e[0] - e[1])**2
    return math.sqrt(s)

def main():
    return

if __name__ == "__main__":
    main()

# EOF.
