#!/usr/bin/python3

# Humam Rashid
# CISC 7700X, Prof. Sverdlov

import sys
import math as m
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
        (1, 1), (1, 2),
        (1, 3), (1, 4),
        (1, 5), (1, 6),
        (1, 7), (1, 8)
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

def log_model(Y):
    X = np.array((
        (1, m.log(1)), (1, m.log(2)),
        (1, m.log(3)), (1, m.log(4)),
        (1, m.log(5)), (1, m.log(6)),
        (1, m.log(7)), (1, m.log(8))
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
    ibm_metrics = {
            'sym': 'IBM',
            'rev_past': np.array((20003.00, 18756.00, 21760.00, 18182.00, \
                    19161.00, 18028.00, 21776.00, 17571.00)),
            'ern_past': np.array((2.61, 2.94, 2.15, 1.78, 2.81, 1.87, 4.11, \
                    1.31)),
            'div_past': np.array((1.57, 1.57, 1.55, 1.57, 1.62, 1.62, 1.62, \
                    1.62))
            }
    msft_metrics = {
            'sym': 'MSFT',
            'rev_past': np.array((30085.00, 29084.00, 32471.00, 30571.00, \
                    33717.00, 33055.00, 36906.00, 35021.00)),
            'ern_past': np.array((1.14, 1.14, 1.08, 1.14, 1.71, 1.38, 1.51, \
                    1.40)),
            'div_past': np.array((0.42, 0.42, 0.46, 0.46, 0.46, 0.46, 0.51, \
                    0.51))
            }
    aapl_metrics = {
            'sym': 'AAPL',
            'rev_past': np.array((53265.00, 62900.00, 84310.00, 58015.00, \
                    53809.00, 64040.00, 91819.00, 58313.00)),
            'ern_past': np.array((0.59, 0.73, 1.05, 0.62, 0.55, 0.76, 1.25, \
                    0.64)),
            'div_past': np.array((0.19, 0.18, 0.19, 0.18, 0.20, 0.19, 0.20, \
                    0.19))
            }
    goog_metrics = {
            'sym': 'GOOG',
            'rev_past': np.array((32657.00, 33740.00, 39276.00, 36339.00, \
                    38944.00, 40499.00, 46075.00, 41159.00)),
            'ern_past': np.array((4.54, 13.06, 12.77, 9.50, 13.21, 10.12, \
                    15.35, 9.87)),
            'div_past': np.array((0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, \
                    0.00))
            }
    fb_metrics = {
            'sym': 'FB',
            'rev_past': np.array((13231.00, 13727.00, 16914.00, 15077.00, \
                    16886.00, 17652.00, 21082.00, 17737.00)),
            'ern_past': np.array((1.74, 1.76, 2.38, 0.85, 0.91, 2.12, 2.56, \
                    1.71)),
            'div_past': np.array((0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, \
                    0.00))
            }
    pg_metrics = {
            'sym': 'PG',
            'rev_past': np.array((16503.00, 16690.00, 17438.00, 16462.00, \
                    17094.00, 17798.00, 18240.00, 17214.00)),
            'ern_past': np.array((0.72, 1.22, 1.22, 1.04, -2.12, 1.36, 1.41, \
                    1.12)),
            'div_past': np.array((0.74, 0.74, 0.74, 0.74, 0.77, 0.77, 0.77, \
                    0.77))
            }
    ge_metrics = {
            'sym': 'GE',
            'rev_past': np.array((29162.00, 23392.00, 16670.00, 22202.00, \
                    23414.00, 23360.00, 26238.00, 20524.00)),
            'ern_past': np.array((0.07, -2.62, 0.07, 0.41, -0.01, -1.08, 0.06, \
                    0.70)),
            'div_past': np.array((0.14, 0.12, 0.14, 0.01, 0.03, 0.01, 0.03, \
                    0.01))
            }
    ############################################################################
    #
    # Next Quarter Revenue, Earnings & Dividends (Linear Model Predictions)
    #
    ############################################################################
    ibm_nextquarter_lin = {
            'rev': lin_model(ibm_metrics['rev']),
            'ern': lin_model(ibm_metrics['ern']),
            'div': abs(lin_model(ibm_metrics['div']))
            }
    msft_nextquarter_lin = {
            'rev': lin_model(msft_metrics['rev']),
            'ern': lin_model(msft_metrics['ern']),
            'div': abs(lin_model(msft_metrics['div']))
            }
    aapl_nextquarter_lin = {
            'rev': lin_model(aapl_metrics['rev']),
            'ern': lin_model(aapl_metrics['ern']),
            'div': abs(lin_model(aapl_metrics['div']))
            }
    goog_nextquarter_lin = {
            'rev': lin_model(goog_metrics['rev']),
            'ern': lin_model(goog_metrics['ern']),
            'div': abs(lin_model(goog_metrics['div']))
            }
    fb_nextquarter_lin = {
            'rev': lin_model(fb_metrics['rev']),
            'ern': lin_model(fb_metrics['ern']),
            'div': abs(lin_model(fb_metrics['div']))
            }
    pg_nextquarter_lin = {
            'rev': lin_model(pg_metrics['rev']),
            'ern': lin_model(pg_metrics['ern']),
            'div': abs(lin_model(pg_metrics['div']))
            }
    ge_nextquarter_lin = {
            'rev': lin_model(ge_metrics['rev']),
            'ern': lin_model(ge_metrics['ern']),
            'div': abs(lin_model(ge_metrics['div']))
            }
    print("Next Quarter Predictions (Linear Model, In Millions USD)\
            \n--------------------------------------------------------\n")
    print_form('IBM', ibm_nextquarter_lin)
    print_form('MSFT', msft_nextquarter_lin)
    print_form('AAPL', aapl_nextquarter_lin)
    print_form('GOOG', goog_nextquarter_lin)
    print_form('FB', fb_nextquarter_lin)
    print_form('PG', pg_nextquarter_lin)
    print_form('GE', ge_nextquarter_lin)
    ############################################################################
    #
    # Next Quarter Revenue, Earnings & Dividends (Logarithmic Model Predictions)
    #
    ############################################################################
    ibm_nextquarter_log = {
            'rev': log_model(ibm_metrics['rev']),
            'ern': log_model(ibm_metrics['ern']),
            'div': abs(log_model(ibm_metrics['div']))
            }
    msft_nextquarter_log = {
            'rev': log_model(msft_metrics['rev']),
            'ern': log_model(msft_metrics['ern']),
            'div': abs(log_model(msft_metrics['div']))
            }
    aapl_nextquarter_log = {
            'rev': log_model(aapl_metrics['rev']),
            'ern': log_model(aapl_metrics['ern']),
            'div': abs(log_model(aapl_metrics['div']))
            }
    goog_nextquarter_log = {
            'rev': log_model(goog_metrics['rev']),
            'ern': log_model(goog_metrics['ern']),
            'div': abs(log_model(goog_metrics['div']))
            }
    fb_nextquarter_log = {
            'rev': log_model(fb_metrics['rev']),
            'ern': log_model(fb_metrics['ern']),
            'div': abs(log_model(fb_metrics['div']))
            }
    pg_nextquarter_log = {
            'rev': log_model(pg_metrics['rev']),
            'ern': log_model(pg_metrics['ern']),
            'div': abs(log_model(pg_metrics['div']))
            }
    ge_nextquarter_log = {
            'rev': log_model(ge_metrics['rev']),
            'ern': log_model(ge_metrics['ern']),
            'div': abs(log_model(ge_metrics['div']))
            }
    print("Next Quarter Predictions (Log. Model, In Millions USD)\
            \n------------------------------------------------------\n")
    print_form('IBM', ibm_nextquarter_log)
    print_form('MSFT', msft_nextquarter_log)
    print_form('AAPL', aapl_nextquarter_log)
    print_form('GOOG', goog_nextquarter_log)
    print_form('FB', fb_nextquarter_log)
    print_form('PG', pg_nextquarter_log)
    print_form('GE', ge_nextquarter_log)

if __name__ == '__main__':
    main()

# EOF.
