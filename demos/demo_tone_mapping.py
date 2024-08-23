"""
%
%       HDR Toolbox demo 1:
%	   1) Load "Bottles_Small.pfm" HDR image
%	   2) Show the image in linear mode
%	   3) Show the image in gamma mode
%	   4) Tone map and show the image using Reinhard's TMO 
%	   5) Show and Apply Color Correction to the tone mapped image
%	   6) Save the tone mapped image as PNG
%
%       Author: Francesco Banterle
%       Copyright February 2011 (c)
%
%
"""

import cv2

from source_code.ColorCorrection.ColorCorrection import ColorCorrection
from source_code.IO.hdrimread import hdrimread
from source_code.Tmo.GammaTMO import GammaTMO
from source_code.Tmo.ReinhardTMO import ReinhardTMO
from source_code.util.imColorOrder import swap_red_blue


def main():
    print("1) Load the image Bottles_Small.pfm using hdrimread")
    img = hdrimread("demos/Bottles_Small.hdr")

    print("2) Show the image Bottles_Small.pfm in linear mode using imshow")
    imgOut = GammaTMO(img, 1.0, 0)
    cv2.imshow("2) HDR visulaization in Linear mode at F-stop 0", swap_red_blue(imgOut))

    print("3) Show the image Bottles_Small.hdr applying gamma")
    imgOut = GammaTMO(img, 2.2, 0)
    cv2.imshow(
        "3) HDR visualization with gamma correction, 2.2, at F-stop 0", swap_red_blue(imgOut)
    )

    print("4) Show the image Bottles_Small.hdr applying Reinhard" "s Tmo")
    imgTMO = ReinhardTMO(img)
    imgOut = GammaTMO(imgTMO, 2.2, 0)
    cv2.imshow("4) Tone mapped image using ReinhardTMO", swap_red_blue(imgOut))

    print("5) Show and Apply Color Correction to the tone mapped image")
    imgTMO = ColorCorrection(imgTMO, 0.5)
    imgOut = GammaTMO(imgTMO, 2.2, 0)
    cv2.imshow("5) Tone mapped image (ReinhardTMO) with color correction", swap_red_blue(imgOut))

    cv2.waitKey()


if __name__ == "__main__":
    main()
