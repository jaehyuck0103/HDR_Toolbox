"""
%
%        imgOut = GammaTMO(img, TMO_gamma, TMO_fstop, TMO_view);
%
%        This function applies exposure (in f-stops) and inverse gamma
%        correction to an image. The function can visualize images if
%        TMO_view is set to true (1).
%
%        Input:
%           -img: image to be tonemapped
%           -TMO_gamma: gamma correction value
%           -TMO_fstop: f-stop value
%           -TMO_view: boolean for displaying the image
%
%        Output:
%           -imgOut: gamma corrected exposure
%
%     Copyright (C) 2011-12  Francesco Banterle
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

from source_code.util.checkNegative import checkNegative


def GammaTMO(img, TMO_gamma=2.2, TMO_fstop=0.0):

    assert TMO_gamma > 0

    checkNegative(img)

    invGamma = 1.0 / TMO_gamma
    exposure = 2**TMO_fstop

    img = (exposure * img) ** invGamma
    img = np.clip(img, 0, 1)

    return img
