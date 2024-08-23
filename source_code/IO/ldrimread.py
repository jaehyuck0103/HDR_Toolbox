import cv2
import numpy as np

from source_code.util.imColorOrder import swap_red_blue

"""
%
%       img = ldrimread(filename, bDouble)
%
%
%        Input:
%           -filename: the name of the file to open
%
%        Output:
%           -img: the opened image
%
%     Copyright (C) 2011-15  Francesco Banterle
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


def ldrimread(filename, bDouble=True):

    img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    orig_dtype = img.dtype

    if bDouble:
        img = img.astype(np.float64)
    else:
        img = img.astype(np.float32)

    if orig_dtype == np.uint8:
        img = img / 255
    elif orig_dtype == np.uint16:
        img = img / 65535
    else:
        raise ValueError(orig_dtype)

    img = swap_red_blue(img)

    return img
