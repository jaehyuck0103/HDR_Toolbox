import numpy as np


def check13Color(img: np.ndarray):

    if img.ndim == 2:
        pass
    elif img.ndim == 3:
        assert img.shape[-1] == 3
    else:
        raise ValueError(img.ndim)
