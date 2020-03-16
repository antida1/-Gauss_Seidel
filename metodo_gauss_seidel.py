# ----------------------------------------------------------------
import numpy as np
import pandas as pd

#GAUSS - SEIDEL


def X1(x2, x3, x5, **kwargs):
    return {'x1': (-x2 - x3 - x5)/4.0 + 3/2.0}


def X2(x1, x3, x4, **kwargs):
    return {'x2': (-x1 + x3 + x4)/3.0 - 2}


def X3(x1, x2, x4, x5, **kwargs):
    return {'x3': (-2*x1 - x2 + x4 + x5)/5.0 + 6/5.0}


def X4(x1, x2, x3, **kwargs):
    return {'x4': (x1 + x2 + x3)/4.0 + 3/2.0}


def X5(x2, x3, x4, **kwargs):
    return {'x5': (-2*x2 + x3 - x4)/4.0 + 3/2.0}


X = {'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0}
A = {'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0}
R = {'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0}
R.update(X1(**A))
A = R.copy()
R.update(X2(**A))
A = R.copy()
R.update(X3(**A))
A = R.copy()
R.update(X4(**A))
A = R.copy()
R.update(X5(**A))
A = R.copy()

W = [X.copy(), R.copy()]

while (np.abs(R['x1'] - X['x1']) > 1e-3) | (
        np.abs(R['x2'] - X['x2']) > 1e-3) | (
        np.abs(R['x3'] - X['x3']) > 1e-3) | (
        np.abs(R['x4'] - X['x4']) > 1e-3) | (
        np.abs(R['x5'] - X['x5']) > 1e-3):
    X = R.copy()
    R.update(X1(**A))
    Aux = R.copy()
    R.update(X2(**A))
    A = R.copy()
    R.update(X3(**A))
    A = R.copy()
    R.update(X4(**A))
    A = R.copy()
    R.update(X5(**A))
    A = R.copy()
    W.append(R.copy())

W = pd.DataFrame(W)
print(W)


# ----------------------------------------------------------------
