import numpy as np


def checkNegative(img):
    assert np.all(img >= 0)
