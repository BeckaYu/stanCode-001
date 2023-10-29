"""
File: mirror_lake.py
Name: Rebecca
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: original_mt, the original image
    :return: reflected, new image that intimates reflection of the original image
    """
    filename = 'images/mt-rainier.jpg'
    original_mt = SimpleImage(filename)
    reflected = SimpleImage.blank(original_mt.width, original_mt.height*2)  # Make a blank canvas with doubled height

    # Get each pixel in the original image
    for x in range(original_mt.width):
        for y in range(original_mt.height):
            original_mt_pixel = original_mt.get_pixel(x, y)

            # Compose the 1st part of the reflected image by copy all pixels of the original image
            reflected_pixel = reflected.get_pixel(x, y)
            reflected_pixel.red = original_mt_pixel.red
            reflected_pixel.green = original_mt_pixel.green
            reflected_pixel.blue = original_mt_pixel.blue

            # Compose the 2nd part of the reflected image by copy all pixels of the original image with revised order
            reflected_pixel = reflected.get_pixel(x, reflected.height-1-y)
            reflected_pixel.red = original_mt_pixel.red
            reflected_pixel.green = original_mt_pixel.green
            reflected_pixel.blue = original_mt_pixel.blue
    return reflected



def main():
    """
    This function creates a reflection of the original image
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
