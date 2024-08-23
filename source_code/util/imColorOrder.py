import numpy as np


# RGB <-> BGR
# RGBA <-> BGRA
def swap_red_blue(img: np.ndarray):

    assert img.ndim == 2 or img.ndim == 3, img.ndim

    if img.ndim == 2:
        pass
    elif img.ndim == 3:
        if img.shape[-1] == 3 or img.shape[-1] == 4:
            img = img[:, :, ::-1]
        elif img.shape[-1] == 4:
            img = img[:, :, [2, 1, 0, 3]]
        else:
            raise ValueError(img.shape[-1])
    else:
        raise ValueError(img.ndim)

    return img
