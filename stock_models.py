#!/usr/bin/python3

# Humam Rashid
# CISC 7700X, Prof. Sverdlov

import sys
import numpy as np
from numpy.linalg import inv

def lin_model(Y):
    X = np.array((
        (1, 1),
        (1, 2),
        (1, 3),
        (1, 4),
        (1, 5),
        (1, 6),
        (1, 7),
        (1, 8)
        ))
    # 1.) X^T * X
    M = np.matmul(X.T, X)
    # 2.) (X^T * X)^-1
    IM = inv(M)
    # 3.) (X^T * X)^-1 * X^T
    M2 = np.matmul(IM, X.T)
    # 4.) (X^T * X)^-1 * X^T * y
    W = np.matmul(M2, Y)
    return round(np.matmul(np.array((1, 9)), W), 2)

def log_model():
    return
def exp_model():
    return
def pow_model():
    return

def main():
    ############################################################################
    #
    # Past 8 Quarters Revenue, Earnings & Dividends
    #
    ############################################################################
    ibm_past8quarters = {
            'rev': np.array((1, 2, 3)),
            'ern': np.array((1, 2, 3)),
            'div': np.array((1, 2, 3))
            }
    msft_past8quarters = {
            'rev': np.array((1, 2, 3)),
            'ern': np.array((1, 2, 3)),
            'div': np.array((1, 2, 3))
            }
    aapl_past8quarters = {
            'rev': np.array((1, 2, 3)),
            'ern': np.array((1, 2, 3)),
            'div': np.array((1, 2, 3))
            }
    goog_past8quarters = {
            'rev': np.array((1, 2, 3)),
            'ern': np.array((1, 2, 3)),
            'div': np.array((1, 2, 3))
            }
    fb_past8quarters = {
            'rev': np.array((13231.00, 13727.00, 16914.00, 15077.00, 16886.00, \
                    17652.00, 21082.00, 17737.00)),
            'ern': np.array((1.74, 1.76, 2.38, 0.85, 0.91, 2.12, 2.56, 1.71)),
            'div': np.array((0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00))
            }
    pg_past8quarters = {
            'rev': np.array((1, 2, 3)),
            'ern': np.array((1, 2, 3)),
            'div': np.array((1, 2, 3))
            }
    ge_past8quarters = {
            'rev': np.array((1, 2, 3)),
            'ern': np.array((1, 2, 3)),
            'div': np.array((1, 2, 3))
            }
    ############################################################################
    #
    # Next Quarter Revenue, Earnings & Dividends (Linear Model)
    #
    ############################################################################
    fb_nextquarter_lin = {
            'rev': lin_model(fb_past8quarters['rev']),
            'ern': lin_model(fb_past8quarters['ern']),
            'div': lin_model(fb_past8quarters['div'])
            }

    print(fb_nextquarter_lin)

if __name__ == '__main__':
    main()

# EOF.
