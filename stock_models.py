#!/usr/bin/python3

# Humam Rashid
# CISC 7700X, Prof. Sverdlov

import math
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
    M = np.matmul(X.T, X)
    IM = inv(M)
    M2 = np.matmul(IM, X.T)
    W = np.matmul(M2, Y)
    pred = np.matmul(np.array((1, 9)), W)
    return round(pred, 3)

def log_model(Y):
    X = np.array((
        (1, math.log(1)),
        (1, math.log(2)),
        (1, math.log(3)),
        (1, math.log(4)),
        (1, math.log(5)),
        (1, math.log(6)),
        (1, math.log(7)),
        (1, math.log(8))
        ))
    M = np.matmul(X.T, X)
    IM = inv(M)
    M2 = np.matmul(IM, X.T)
    W = np.matmul(M2, Y)
    pred = np.matmul(np.array((1, math.log(9))), W)
    return round(pred, 3)

def exp_model(Y):
    Y_ln = []
    for i in Y:
        Y_ln.append(math.log(abs(i)))
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
    M = np.matmul(X.T, X)
    IM = inv(M)
    M2 = np.matmul(IM, X.T)
    W = np.matmul(M2, Y_ln)
    W[1] = math.exp(W[1])
    pred = np.matmul(np.array((1, 9)), W)
    return round(pred, 3)

def pow_model(Y):
    Y_ln = []
    for i in Y:
        Y_ln.append(math.log(abs(i)))
    X = np.array((
        (1, math.log(1)),
        (1, math.log(2)),
        (1, math.log(3)),
        (1, math.log(4)),
        (1, math.log(5)),
        (1, math.log(6)),
        (1, math.log(7)),
        (1, math.log(8))
        ))
    M = np.matmul(X.T, X)
    IM = inv(M)
    M2 = np.matmul(IM, X.T)
    W = np.matmul(M2, Y_ln)
    W[1] = math.exp(W[1])
    pred = np.matmul(np.array((1, math.log(9))), W)
    return round(pred, 3)

def r_squared(Y, P):
    mean_observed = sum(Y) / len(Y)
    squares = []
    for i in Y:
        squares.append((i - mean_observed) ** 2)
    total_sum_sq = sum(squares)
    squares = []
    for i in range(len(Y)):
        squares.append((Y[i] - P[i]) ** 2)
    sum_sq_residuals = sum(squares)
    return round((1 - (sum_sq_residuals / total_sum_sq)), 3)

def grade_bysym(metric, pos):
    Y = []
    Plin = []
    Plog = []
    Pexp = []
    Ppow = []
    r_sqs = dict()
    Y.append(metric['rev_9qtr'][pos - 1])
    Y.append(metric['ern_9qtr'][pos - 1])
    if metric['div_9qtr'] is None:
        Y.append(0.00)
    else:
        Y.append(metric['div_9qtr'][pos - 1])
    Plin.append(metric['rev_next']['lin'])
    Plin.append(metric['ern_next']['lin'])
    Plin.append(metric['div_next']['lin']) 
    Plog.append(metric['rev_next']['log'])
    Plog.append(metric['ern_next']['log'])
    Plog.append(metric['div_next']['log'])
    Pexp.append(metric['rev_next']['exp'])
    Pexp.append(metric['ern_next']['exp'])
    Pexp.append(metric['div_next']['exp'])
    Ppow.append(metric['rev_next']['pow'])
    Ppow.append(metric['ern_next']['pow'])
    Ppow.append(metric['div_next']['pow'])
    r_sq_lin = r_squared(Y, Plin)
    r_sq_log = r_squared(Y, Plog)
    r_sq_exp = r_squared(Y, Pexp)
    r_sq_pow = r_squared(Y, Ppow)
    r_sqs[r_sq_lin] = "Linear"
    r_sqs[r_sq_log] = "Logarithmic"
    r_sqs[r_sq_exp] = "Exponential"
    r_sqs[r_sq_pow] = "Power"
    s = f"\tR-Squared:\
            \n\t\tLin. model: {r_sq_lin}\
            \n\t\tLog. model: {r_sq_log}\
            \n\t\tExp. model: {r_sq_exp}\
            \n\t\tPow. model: {r_sq_pow}\
            \n\n\t\tBest model for {metric['sym']}: {r_sqs[max(list(r_sqs))]}\n"
    print(s)

def grade_bymetric():
    return

def print_metrics(m):
    s = f"Symbol: {m['sym']}\
            \n\tRevenue:\
            \n\t\tLin. model: {m['rev_next']['lin']},\
            \n\t\terror: {m['rev_err']['lin']}\n\
            \n\t\tLog. model: {m['rev_next']['log']},\
            \n\t\terror: {m['rev_err']['log']}\n\
            \n\t\tExp. model: {m['rev_next']['exp']},\
            \n\t\terror: {m['rev_err']['exp']}\n\
            \n\t\tPow. model: {m['rev_next']['pow']},\
            \n\t\terror: {m['rev_err']['pow']}\n\
            \n\tEarnings:\
            \n\t\tLin. model: {m['ern_next']['lin']},\
            \n\t\terror: {m['ern_err']['lin']}\n\
            \n\t\tLog. model: {m['ern_next']['log']},\
            \n\t\terror: {m['ern_err']['log']}\n\
            \n\t\tExp. model: {m['ern_next']['exp']},\
            \n\t\terror: {m['ern_err']['exp']}\n\
            \n\t\tPow. model: {m['ern_next']['pow']},\
            \n\t\terror: {m['ern_err']['pow']}\n\
            \n\tDividends:\
            \n\t\tLin. model: {abs(m['div_next']['lin'])},\
            \n\t\terror: {m['div_err']['lin']}\n\
            \n\t\tLog. model: {abs(m['div_next']['log'])},\
            \n\t\terror: {m['div_err']['log']}\n\
            \n\t\tExp. model: {abs(m['div_next']['exp'])},\
            \n\t\terror: {m['div_err']['exp']}\n\
            \n\t\tPow. model: {abs(m['div_next']['pow'])},\
            \n\t\terror: {m['div_err']['pow']}\n"
    print(s)

def prediction_error(m, pos):
    m['rev_err'] = {
            'lin': round(m['rev_9qtr'][pos - 1] - m['rev_next']['lin'], 3),
            'log': round(m['rev_9qtr'][pos - 1] - m['rev_next']['log'], 3),
            'exp': round(m['rev_9qtr'][pos - 1] - m['rev_next']['exp'], 3),
            'pow': round(m['rev_9qtr'][pos - 1] - m['rev_next']['pow'], 3)
            }
    m['ern_err'] = {
            'lin': round(m['ern_9qtr'][pos - 1] - m['ern_next']['lin'], 3),
            'log': round(m['ern_9qtr'][pos - 1] - m['ern_next']['log'], 3),
            'exp': round(m['ern_9qtr'][pos - 1] - m['ern_next']['exp'], 3),
            'pow': round(m['ern_9qtr'][pos - 1] - m['ern_next']['pow'], 3)
            }
    if m['div_9qtr'] is None:
        m['div_err'] = {
                'lin': 0.00,
                'log': 0.00,
                'exp': 0.00,
                'pow': 0.00
                }
    else:
        m['div_err'] = {
                'lin': round(m['div_9qtr'][pos - 1] - m['div_next']['lin'], 3),
                'log': round(m['div_9qtr'][pos - 1] - m['div_next']['log'], 3),
                'exp': round(m['div_9qtr'][pos - 1] - m['div_next']['exp'], 3),
                'pow': round(m['div_9qtr'][pos - 1] - m['div_next']['log'], 3)
                }

def predicted_metrics(m, start, end):
    m['rev_next'] = {
            'lin': lin_model(m['rev_9qtr'][start:end]),
            'log': log_model(m['rev_9qtr'][start:end]),
            'exp': exp_model(m['rev_9qtr'][start:end]),
            'pow': pow_model(m['rev_9qtr'][start:end])
            }
    m['ern_next'] = {
            'lin': lin_model(m['ern_9qtr'][start:end]),
            'log': log_model(m['ern_9qtr'][start:end]),
            'exp': exp_model(m['ern_9qtr'][start:end]),
            'pow': pow_model(m['ern_9qtr'][start:end])
            }
    if m['div_9qtr'] is None:
        m['div_next'] = {
                'lin': 0.00,
                'log': 0.00,
                'exp': 0.00,
                'pow': 0.00
                }
    else:
        m['div_next'] = {
                'lin': lin_model(m['div_9qtr'][start:end]),
                'log': log_model(m['div_9qtr'][start:end]),
                'exp': exp_model(m['div_9qtr'][start:end]),
                'pow': pow_model(m['div_9qtr'][start:end])
                }

def main():
    ############################################################################
    #
    # Past 9 Quarters Revenue, Earnings & Dividends.
    #
    # (Numbers used are from (Q2, 2018) to (Q2, 2020), inclusive)
    #
    ############################################################################
    ibm_metrics = {
            'sym': 'IBM',
            'rev_9qtr': np.array((20003.00, 18756.00, 21760.00, 18182.00, \
                    19161.00, 18028.00, 21776.00, 17571.00, 18123.00)),
            'ern_9qtr': np.array((2.61, 2.94, 2.15, 1.78, 2.81, 1.87, 4.11, \
                    1.31, 1.52)),
            'div_9qtr': np.array((1.57, 1.57, 1.55, 1.57, 1.62, 1.62, 1.62, \
                    1.62, 1.63))
            }
    msft_metrics = {
            'sym': 'MSFT',
            'rev_9qtr': np.array((30085.00, 29084.00, 32471.00, 30571.00, \
                    33717.00, 33055.00, 36906.00, 35021.00, 38033.00)),
            'ern_9qtr': np.array((1.14, 1.14, 1.08, 1.14, 1.71, 1.38, 1.51, \
                    1.40, 1.46)),
            'div_9qtr': np.array((0.42, 0.42, 0.46, 0.46, 0.46, 0.46, 0.51, \
                    0.51, 0.51))
            }
    aapl_metrics = {
            'sym': 'AAPL',
            'rev_9qtr': np.array((53265.00, 62900.00, 84310.00, 58015.00, \
                    53809.00, 64040.00, 91819.00, 58313.00, 59685.00)),
            'ern_9qtr': np.array((0.59, 0.73, 1.05, 0.62, 0.55, 0.76, 1.25, \
                    0.64, 0.65)),
            'div_9qtr': np.array((0.19, 0.18, 0.19, 0.18, 0.20, 0.19, 0.20, \
                    0.19, 0.21))
            }
    goog_metrics = {
            'sym': 'GOOG',
            'rev_9qtr': np.array((32657.00, 33740.00, 39276.00, 36339.00, \
                    38944.00, 40499.00, 46075.00, 41159.00, 38297.00)),
            'ern_9qtr': np.array((4.54, 13.06, 12.77, 9.50, 13.21, 10.12, \
                    15.35, 9.87, 10.13)),
            'div_9qtr': None
            }
    fb_metrics = {
            'sym': 'FB',
            'rev_9qtr': np.array((13231.00, 13727.00, 16914.00, 15077.00, \
                    16886.00, 17652.00, 21082.00, 17737.00, 18687.00)),
            'ern_9qtr': np.array((1.74, 1.76, 2.38, 0.85, 0.91, 2.12, 2.56, \
                    1.71, 1.80)),
            'div_9qtr': None
            }
    pg_metrics = {
            'sym': 'PG',
            'rev_9qtr': np.array((16503.00, 16690.00, 17438.00, 16462.00, \
                    17094.00, 17798.00, 18240.00, 17214.00, 17698.00)),
            'ern_9qtr': np.array((0.72, 1.22, 1.22, 1.04, -2.12, 1.36, 1.41, \
                    1.12, 1.07)),
            'div_9qtr': np.array((0.74, 0.74, 0.74, 0.74, 0.77, 0.77, 0.77, \
                    0.77, 0.82))
            }
    ge_metrics = {
            'sym': 'GE',
            'rev_9qtr': np.array((29162.00, 23392.00, 16670.00, 22202.00, \
                    23414.00, 23360.00, 26238.00, 20524.00, 17750.00)),
            'ern_9qtr': np.array((0.07, -2.62, 0.07, 0.41, -0.01, -1.08, 0.06, \
                    0.70, -0.26)),
            'div_9qtr': np.array((0.14, 0.12, 0.14, 0.01, 0.03, 0.01, 0.03, \
                    0.01, 0.03))
            }
    metrics = [ibm_metrics, msft_metrics, aapl_metrics, goog_metrics, \
            fb_metrics, pg_metrics, ge_metrics]
    ############################################################################
    #
    # Next Quarter Revenue, Earnings & Dividends (Predicted)
    #
    # (Based on the first 8 oberved values)
    #
    ############################################################################
    print("Next Quarter Predictions (In Millions USD)\
           \n------------------------------------------\n")
    for m in metrics:
       predicted_metrics(m, 0, 8)
       prediction_error(m, 9)
       print_metrics(m)
       grade_bysym(m, 9)

if __name__ == '__main__':
    main()

# EOF.
