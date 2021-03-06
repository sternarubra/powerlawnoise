# Copyright (C) 2020 by Landmark Acoustics LLC
r'''An autoregressive model for generating power-law noise.

The method here is outlined in Kasdin, N. J. and T. Walter. 1992. "Discrete
simulation of power law noise." Proc. 1992 IEEE Frequency Control Symposium.
Hershey, PA. pp 274-283.

'''

import itertools

import numpy as np


def generate_ar_coefficients(alpha: float) -> float:
    r'''Coefficients for a discrete autoregressive model of power law noise.

    Parameters
    ----------
    alpha : float
        The exponent of the power law. Its spectrum will have this slope on a
        log-log plot.

    Yields
    ------
    h : float
        The next coefficient in the model. Starts with h_1 because h_0 is one.

    '''

    h = 1.0
    yield h
    g = -1.0 + 0.5*alpha
    for k in itertools.count(1):
        g += 1.0
        h *= g/k
        yield -h


def coefficient_array(alpha: float, degree: int) -> np.ndarray:
    r'''Finds the array and returns it without h_0, which is always 1.

    Parameters
    ----------
    alpha : float
        see `generate_ar_coefficients`.

    degree : int
        The length that the input needs to be.

    Returns
    -------
    np.ndarray : the coefficents of a power-law autoregressive model

    The coefficients are in reverse order. The array's format is
        [h[degree], h[degree-1], ... h[2], h[1]].

    '''

    return np.array([x[0] for x in zip(generate_ar_coefficients(alpha),
                                       range(degree + 1))])
