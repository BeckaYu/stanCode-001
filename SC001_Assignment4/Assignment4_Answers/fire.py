"""
File: fire.py
Name: Rebecca
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: original_fire, the original image
    :return: highlighted_fire, updated image with fire been highlighted
    """
    filename = 'images/greenland-fire.png'
    highlighted_fire = SimpleImage(filename)
    for pixel in highlighted_fire:
        grey_scale = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red > grey_scale * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = grey_scale
            pixel.green = grey_scale
            pixel.blue = grey_scale
    return highlighted_fire


def main():
    """
    This function helps change the color of the photos to highlight fire.
    The result will be a new photo with only fire being colored in red, others become grey.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
