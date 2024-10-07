"""
%
%        imgOut = LogarithmicTMO(img, log_q, log_k)  
%
%
%       Input:
%           -img: input HDR image
%           -log_q: appearance value (1, +inf)
%           -log_k: appearance value (1, +inf)
%
%       Output
%           -imgOut: tone mapped image
% 
%     Copyright (C) 2006-2010 Francesco Banterle
% 
%     This program is free software: you can redistribute it and/or modify
%     it under the terms of the GNU General Public License as published by
%     the Free Software Foundation, either version 3 of the License, or
%     (at your option) any later version.
% 
%     This program is distributed in the hope that it will be useful,
%     but WITHOUT ANY WARRANTY; without even the implied warranty of
%     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
%     GNU General Public License for more details.
% 
%     You should have received a copy of the GNU General Public License
%     along with this program.  If not, see <http://www.gnu.org/licenses/>.
%
"""

import numpy as np

from source_code.ColorSpace.lum import lum
from source_code.Tmo.util.ChangeLuminance import ChangeLuminance
from source_code.util.check13Color import check13Color
from source_code.util.checkNegative import checkNegative


def LogarithmicTMO(img, log_q=1.0, log_k=1.0):

    check13Color(img)
    checkNegative(img)

    assert log_q >= 1
    assert log_k >= 1

    L = lum(img)

    # dynamic range reduction
    Ld = np.log10(1 + L * log_q) / np.log10(1 + L.max() * log_k)

    # change luminance in img
    imgOut = ChangeLuminance(img, L, Ld)

    return imgOut


if __name__ == "__main__":

    import cv2

    from source_code.IO.hdrimread import hdrimread
    from source_code.Tmo.GammaTMO import GammaTMO
    from source_code.util.imColorOrder import swap_red_blue

    img = hdrimread("demos/Bottles_Small.hdr")
    imgTMO = LogarithmicTMO(img, log_q=10.0)
    imgOut = GammaTMO(imgTMO, 2.2, 0)
    cv2.imshow("Tone mapped image using LogarthmicTMO", swap_red_blue(imgOut))
    cv2.waitKey()
