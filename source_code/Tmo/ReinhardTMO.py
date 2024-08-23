"""
%
%
%      [imgOut, pAlpha, pWhite] = ReinhardTMO(img, pAlpha, pWhite, pLocal, pPhi)
%
%
%       Input:
%           -img: input HDR image
%           -pAlpha: value of exposure of the image
%           -pWhite: the white point 
%           -pLocal: local mode
%                 - 'global': the method will not compute local adaptation
%                 - 'local': the method will compute classic local
%                 adaptation as in the original paper
%                 - 'bilateral': the method will compute local adaptation
%                 using the bilateral filter
%           -pPhi: a parameter which controls the sharpening
%
%       Output:
%           -imgOut: output tone mapped image in linear domain
%           -pAlpha: as in input
%           -pLocal: as in input 
%
%     Copyright (C) 2011-17  Francesco Banterle
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
%     The paper describing this technique is:
%     "Photographic Tone Reproduction for Digital Images"
% 	  by Erik Reinhard, Michael Stark, Peter Shirley, James Ferwerda
%     in Proceedings of SIGGRAPH 2002
%
"""

from source_code.ColorSpace.lum import lum
from source_code.Tmo.util.ChangeLuminance import ChangeLuminance
from source_code.Tmo.util.logMean import logMean
from source_code.Tmo.util.ReinhardAlpha import ReinhardAlpha
from source_code.Tmo.util.ReinhardWhitePoint import ReinhardWhitePoint
from source_code.util.check13Color import check13Color


def ReinhardTMO(img, pAlpha=None, pWhite=None, pLocal="global", pPhi=8, Lwa=None):

    check13Color(img)

    # Luminance channel
    L = lum(img)

    if pAlpha is None:
        pAlpha = ReinhardAlpha(L)

    if pWhite is None:
        pWhite = ReinhardWhitePoint(L)

    # compute logarithmic mean
    if Lwa is None:
        Lwa = logMean(L)

    assert pAlpha > 0
    assert pWhite > 0
    assert pPhi >= 0
    assert Lwa >= 0

    # scale luminance using alpha and logarithmic mean
    Lscaled = (pAlpha * L) / Lwa

    # compute adaptation
    if pLocal == "global":
        L_adapt = Lscaled
    elif pLocal == "local":
        L_adapt = ReinhardFiltering(Lscaled, pAlpha, pPhi)
    elif pLocal == "bilateral":
        L_adapt = ReinhardBilateralFiltering(Lscaled, pAlpha, pPhi)
    elif pLocal == "mean":
        L_adapt = filterGaussian(Lscaled, pPhi)
    else:
        raise ValueError(pLocal)

    # range compression
    Ld = (Lscaled * (1 + Lscaled / pWhite**2)) / (1 + L_adapt)

    # change luminance
    imgOut = ChangeLuminance(img, L, Ld)

    return imgOut
