#!/usr/bin/python3

# Humam Rashid
# CISC 7700X, Prof. Sverdlov

import sys
import math as m
import numpy as np
from numpy.linalg import inv

def lin_model(Y):
    X = np.array((
        (1, 1), (1, 2),
        (1, 3), (1, 4),
        (1, 5), (1, 6),
        (1, 7), (1, 8)
        ))
    M = np.matmul(X.T, X)
    IM = inv(M)
    M2 = np.matmul(IM, X.T)
    W = np.matmul(M2, Y)
    pred = np.matmul(np.array((1, 9)), W)
    return round(pred, 3)

def log_model(Y):
    X = np.array((
        (1, m.log(1)), (1, m.log(2)),
        (1, m.log(3)), (1, m.log(4)),
        (1, m.log(5)), (1, m.log(6)),
        (1, m.log(7)), (1, m.log(8))
        ))
    M = np.matmul(X.T, X)
    IM = inv(M)
    M2 = np.matmul(IM, X.T)
    W = np.matmul(M2, Y)
    pred = np.matmul(np.array((1, m.log(9))), W)
    return round(pred, 3)

def exp_model(Y):
    Y_ln = []
    for i in Y:
        Y_ln.append(m.log(i))
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
    W = np.matmul(M2, Y_ln)
    # Next quarter prediction
    print("exp(B) = ", m.exp(W[1]))
    W[1] = m.exp(W[1])
    print("B = ", W[1])
    pred = np.matmul(np.array((1, 9)), W)
    return round(pred, 3)

def pow_model(Y):
    return 0

def print_metrics(m):
    s = f"""Symbol: {m['sym']}\
            \n\n\tRevenue:\
            \n\t\tLin. model: {m['rev_next']['lin']}\
            \n\t\tLog. model: {m['rev_next']['log']}\
            \n\t\tExp. model: {m['rev_next']['exp']}\
            \n\t\tPow. model: {m['rev_next']['pow']}\
            \n\tEarnings:\
            \n\t\tLin. model: {m['ern_next']['lin']}\
            \n\t\tLog. model: {m['ern_next']['log']}\
            \n\t\tExp. model: {m['ern_next']['exp']}\
            \n\t\tPow. model: {m['ern_next']['pow']}\
            \n\tDividends:\
            \n\t\tLin. model: {abs(m['div_next']['lin'])}\
            \n\t\tLog. model: {abs(m['div_next']['log'])}\
            \n\t\tExp. model: {abs(m['div_next']['exp'])}\
            \n\t\tPow. model: {abs(m['div_next']['pow'])}\
            \n"""
    print(s)

def load_preds(m):
    m['rev_next'] = {
            'lin': lin_model(m['rev_past']),
            'log': log_model(m['rev_past']),
            'exp': exp_model(m['rev_past']),
            'pow': pow_model(m['rev_past'])
            }
    m['ern_next'] = {
            'lin': lin_model(m['ern_past']),
            'log': log_model(m['ern_past']),
            'exp': exp_model(m['ern_past']),
            'pow': pow_model(m['ern_past'])
            }
    m['div_next'] = {
            'lin': lin_model(m['div_past']),
            'log': log_model(m['div_past']),
            'exp': exp_model(m['div_past']),
            'pow': pow_model(m['div_past'])
            }

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
    metrics = [ibm_metrics, msft_metrics, aapl_metrics, goog_metrics, \
            fb_metrics, pg_metrics, ge_metrics]
    ############################################################################
    #
    # Next Quarter Revenue, Earnings & Dividends (Predicted)
    #
    ############################################################################
    for m in metrics:
       load_preds(m)
    print("Next Quarter Predictions (In Millions USD)\
            \n------------------------------------------\n")
    for m in metrics:
       print_metrics(m)

if __name__ == '__main__':
    main()

# EOF.
