import numpy as np

"""
%
%
%       img = RemoveSpecials(img, clamping_value)
%
%       This function removes specials: Inf and NaN
%
%       Input:
%           -img: an image which can contain float special values
%           -clamping_value:
%
%       Output:
%           -img: the image without float special values
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


def RemoveSpecials(img, clamping_value=0):
    return np.nan_to_num(img, nan=clamping_value, posinf=clamping_value, neginf=clamping_value)
