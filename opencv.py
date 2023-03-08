import cv2
import enum
import numpy as np
from typing import List


class ImreadModes(enum.Enum):
    """ If set, return the loaded image as is (with alpha channel, otherwise it gets cropped). Ignore EXIF orientation. """
    IMREAD_UNCHANGED = cv2.IMREAD_UNCHANGED

    """ If set, always convert image to the single channel grayscale image (codec internal conversion). """
    IMREAD_GRAYSCALE = cv2.IMREAD_GRAYSCALE

    """ If set, always convert image to the 3 channel BGR color image. """
    IMREAD_COLOR = cv2.IMREAD_COLOR

    """ If set, return 16-bit/32-bit image when the input has the corresponding depth, otherwise convert it to 8-bit. """
    IMREAD_ANYDEPTH = cv2.IMREAD_ANYDEPTH

    """ If set, the image is read in any possible color format. """
    IMREAD_ANYCOLOR = cv2.IMREAD_ANYCOLOR

    """ If set, use the gdal driver for loading the image. """
    IMREAD_LOAD_GDAL = cv2.IMREAD_LOAD_GDAL

    """ If set, always convert image to the single channel grayscale image and the image size reduced 1/2. """
    IMREAD_REDUCED_GRAYSCALE_2 = cv2.IMREAD_REDUCED_GRAYSCALE_2

    """ If set, always convert image to the 3 channel BGR color image and the image size reduced 1/2. """
    IMREAD_REDUCED_COLOR_2 = cv2.IMREAD_REDUCED_COLOR_2

    """ If set, always convert image to the single channel grayscale image and the image size reduced 1/4. """
    IMREAD_REDUCED_GRAYSCALE_4 = cv2.IMREAD_REDUCED_GRAYSCALE_4

    """ If set, always convert image to the 3 channel BGR color image and the image size reduced 1/4. """
    IMREAD_REDUCED_COLOR_4 = cv2.IMREAD_REDUCED_COLOR_4

    """ If set, always convert image to the single channel grayscale image and the image size reduced 1/8. """
    IMREAD_REDUCED_GRAYSCALE_8 = cv2.IMREAD_REDUCED_GRAYSCALE_8

    """ If set, always convert image to the 3 channel BGR color image and the image size reduced 1/8. """
    IMREAD_REDUCED_COLOR_8 = cv2.IMREAD_REDUCED_COLOR_8

    """ If set, do not rotate the image according to EXIF's orientation flag. """
    IMREAD_IGNORE_ORIENTATION = cv2.IMREAD_IGNORE_ORIENTATION


class ImwriteFlags(enum.Enum):
    """ For JPEG, it can be a quality from 0 to 100 (the higher is the better). Default value is 95. """
    IMWRITE_JPEG_QUALITY = cv2.IMWRITE_JPEG_QUALITY

    """ Enable JPEG features, 0 or 1, default is False. """
    IMWRITE_JPEG_PROGRESSIVE = cv2.IMWRITE_JPEG_PROGRESSIVE

    """ Enable JPEG features, 0 or 1, default is False. """
    IMWRITE_JPEG_OPTIMIZE = cv2.IMWRITE_JPEG_OPTIMIZE

    """ JPEG restart interval, 0 - 65535, default is 0 - no restart. """
    IMWRITE_JPEG_RST_INTERVAL = cv2.IMWRITE_JPEG_RST_INTERVAL

    """ Separate luma quality level, 0 - 100, default is -1 - don't use. """
    IMWRITE_JPEG_LUMA_QUALITY = cv2.IMWRITE_JPEG_LUMA_QUALITY

    """ Separate chroma quality level, 0 - 100, default is -1 - don't use. """
    IMWRITE_JPEG_CHROMA_QUALITY = cv2.IMWRITE_JPEG_CHROMA_QUALITY

    """ For JPEG, set sampling factor. See cv::ImwriteJPEGSamplingFactorParams. """
    IMWRITE_JPEG_SAMPLING_FACTOR = cv2.IMWRITE_JPEG_SAMPLING_FACTOR

    """ For PNG, it can be the compression level from 0 to 9. A higher value means a smaller size and longer compression time. If specified, strategy is changed to IMWRITE_PNG_STRATEG """
    IMWRITE_PNG_COMPRESSION = cv2.IMWRITE_PNG_COMPRESSION


def imread(filename: str, flags: ImreadModes = ImreadModes.IMREAD_COLOR) -> np.ndarray:
    return cv2.imread(filename, flags.value)


def imwrite(filename: str, image: np.ndarray, params: List[ImreadModes] = None) -> bool:
    params = params or []
    return cv2.imwrite(filename, image, params)
