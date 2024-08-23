"""
%
%       imgOut = ChangeLuminance(img, Lold, Lnew, bEpsilon)
%
%
%       Input:
%           -img: input image
%           -Lold: old luminance
%           -Lnew: new luminance
%           -bEpsilon: a boolean value to avoid division by zero, 
%                      this add e=1e-6 to Lold
%
%       Output
%           -imgOut: output image with Lnew luminance
% 
%     Copyright (C) 2013-2023  Francesco Banterle
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

from source_code.util.RemoveSpecials import RemoveSpecials


def ChangeLuminance(img, Lold, Lnew, bEpsilon=False):

    if bEpsilon:
        Lold = Lold + 1e-6

    img = img * Lnew[:, :, np.newaxis] / Lold[:, :, np.newaxis]
    img = RemoveSpecials(img)

    return img
