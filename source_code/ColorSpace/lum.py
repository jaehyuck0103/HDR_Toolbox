import numpy as np


def lum(img: np.ndarray):

    if img.ndim == 2:
        L = img
    elif img.ndim == 3:
        if img.shape[2] == 3:
            L = 0.2126 * img[:, :, 0] + 0.7152 * img[:, :, 1] + 0.0722 * img[:, :, 2]
        else:
            L = img.mean(2)
            print("Warning: Mean of channels was computed")
            print("Warning: The input image is not an RGB or luminance image!")
    else:
        raise ValueError(img.ndim)

    return L
