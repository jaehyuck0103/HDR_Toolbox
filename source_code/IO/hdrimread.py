"""
%
%       [img, hdr_info] = hdrimread(filename)
%
%       This function reads from a file with name filename an HDR image, if
%       the format can not be opened, it tries to open it as it was an LDR
%       image using imread from MATLAB Image Processing Toolbox.
%
%       NOTE: JPEG2000 file passed as input are meant to be compressed
%       using HDR JPEG-2000. 
%
%        Input:
%           -filename: the name of the file to open
%
%        Output:
%           -img: the opened image
%           -hdr_info: RGBE format extra datum such as: exposure, gamma, etc.
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

import cv2
import numpy as np

from source_code.util.imColorOrder import swap_red_blue
from source_code.util.RemoveSpecials import RemoveSpecials


def hdrimread(filename):

    img = cv2.imread(str(filename), cv2.IMREAD_UNCHANGED)
    img = img.astype(np.float64)

    img = RemoveSpecials(img)
    img = swap_red_blue(img)

    return img
