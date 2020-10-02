#!/usr/bin/python3

# Humam Rashid
# CISC 7700X, Prof. Sverdlov

import sys
import numpy as np
from numpy.linalg import inv

def print_form(sym, vals):
    s = f"""{sym}:\
            \n\tRevenue:\t{vals['rev']}\
            \n\tEarnings:\t{vals['ern']}\
            \n\tDividends:\t{vals['div']}\
            \n"""
    print(s)

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
            'rev': np.array((20003.00, 18756.00, 21760.00, 18182.00, 19161.00, \
                18028.00, 21776.00, 17571.00)),
            'ern': np.array((2.61, 2.94, 2.15, 1.78, 2.81, 1.87, 4.11, 1.31)),
            'div': np.array((1.57, 1.57, 1.55, 1.57, 1.62, 1.62, 1.62, 1.62))
            }
    msft_past8quarters = {
            'rev': np.array((30085.00, 29084.00, 32471.00, 30571.00, 33717.00, \
                    33055.00, 36906.00, 35021.00)),
            'ern': np.array((1.14, 1.14, 1.08, 1.14, 1.71, 1.38, 1.51, 1.40)),
            'div': np.array((0.42, 0.42, 0.46, 0.46, 0.46, 0.46, 0.51, 0.51))
            }
    aapl_past8quarters = {
            'rev': np.array((53265.00, 62900.00, 84310.00, 58015.00, 53809.00, \
                    64040.00, 91819.00, 58313.00)),
            'ern': np.array((0.59, 0.73, 1.05, 0.62, 0.55, 0.76, 1.25, 0.64)),
            'div': np.array((0.19, 0.18, 0.19, 0.18, 0.20, 0.19, 0.20, 0.19))
            }
    goog_past8quarters = {
            'rev': np.array((32657.00, 33740.00, 39276.00, 36339.00, 38944.00, \
                    40499.00, 46075.00, 41159.00)),
            'ern': np.array((4.54, 13.06, 12.77, 9.50, 13.21, 10.12, 15.35, 9.87)),
            'div': np.array((0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00))
            }
    fb_past8quarters = {
            'rev': np.array((13231.00, 13727.00, 16914.00, 15077.00, 16886.00, \
                    17652.00, 21082.00, 17737.00)),
            'ern': np.array((1.74, 1.76, 2.38, 0.85, 0.91, 2.12, 2.56, 1.71)),
            'div': np.array((0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00))
            }
    pg_past8quarters = {
            'rev': np.array((16503.00, 16690.00, 17438.00, 16462.00, 17094.00, \
                    17798.00, 18240.00, 17214.00)),
            'ern': np.array((0.72, 1.22, 1.22, 1.04, 2.12, 1.36, 1.41, 1.12)),
            'div': np.array((0.74, 0.74, 0.74, 0.74, 0.77, 0.77, 0.77, 0.77))
            }
    ge_past8quarters = {
            'rev': np.array((1, 2, 3)),
            'ern': np.array((1, 2, 3)),
            'div': np.array((1, 2, 3))
            }
    ############################################################################
    #
    # Next Quarter Revenue, Earnings & Dividends (Linear Model Predictions)
    #
    ############################################################################
    ibm_nextquarter_lin = {
            'rev': lin_model(ibm_past8quarters['rev']),
            'ern': lin_model(ibm_past8quarters['ern']),
            'div': lin_model(ibm_past8quarters['div'])
            }
    msft_nextquarter_lin = {
            'rev': lin_model(msft_past8quarters['rev']),
            'ern': lin_model(msft_past8quarters['ern']),
            'div': lin_model(msft_past8quarters['div'])
            }
    aapl_nextquarter_lin = {
            'rev': lin_model(aapl_past8quarters['rev']),
            'ern': lin_model(aapl_past8quarters['ern']),
            'div': lin_model(aapl_past8quarters['div'])
            }
    goog_nextquarter_lin = {
            'rev': lin_model(goog_past8quarters['rev']),
            'ern': lin_model(goog_past8quarters['ern']),
            'div': lin_model(goog_past8quarters['div'])
            }
    fb_nextquarter_lin = {
            'rev': lin_model(fb_past8quarters['rev']),
            'ern': lin_model(fb_past8quarters['ern']),
            'div': lin_model(fb_past8quarters['div'])
            }
    pg_nextquarter_lin = {
            'rev': lin_model(pg_past8quarters['rev']),
            'ern': lin_model(pg_past8quarters['ern']),
            'div': lin_model(pg_past8quarters['div'])
            }
    print("Next Quarter Predictions (Linear Model, In Millions USD)\
            \n--------------------------------------------------------\n")
    print_form('IBM', ibm_nextquarter_lin)
    print_form('MSFT', msft_nextquarter_lin)
    print_form('AAPL', aapl_nextquarter_lin)
    print_form('GOOG', goog_nextquarter_lin)
    print_form('FB', fb_nextquarter_lin)
    print_form('PG', pg_nextquarter_lin)

if __name__ == '__main__':
    main()

# EOF.
