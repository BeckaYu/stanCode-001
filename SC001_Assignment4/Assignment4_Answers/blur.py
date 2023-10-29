"""
File: blur.py
Name: Rebecca
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: old img, the original image
    :return: blurred img, the blurred image
    """
    # Todo: create a new blank img that is as big as the original one
    filepath = "images/smiley-face.png"
    img = SimpleImage(filepath)
    blurred_img = SimpleImage(filepath)
    blurred_img = blurred_img.blank(blurred_img.width, blurred_img.height)

    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.

            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                blurred_img_pixel = blurred_img.get_pixel(x, y)

                # Define the variables of surrounded pixels
                pixel = img.get_pixel(x, y)
                pixel_b = img.get_pixel(x, y + 1)
                pixel_r = img.get_pixel(x + 1, y)
                pixel_br = img.get_pixel(x + 1, y + 1)

                # Make pixel (0,0) blurred
                blurred_img_pixel.red = (pixel.red + pixel_b.red + pixel_r.red + pixel_br.red) // 4
                blurred_img_pixel.green = (pixel.green + pixel_b.green + pixel_r.green + pixel_br.green) // 4
                blurred_img_pixel.blue = (pixel.blue + pixel_b.blue + pixel_r.blue + pixel_br.blue) // 4

            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                blurred_img_pixel = blurred_img.get_pixel(x, y)

                # Define the variables of surrounded pixels
                pixel = img.get_pixel(x, y)
                pixel_l = img.get_pixel(x - 1, y)
                pixel_bl = img.get_pixel(x - 1, y + 1)
                pixel_b = img.get_pixel(x, y + 1)

                # Make a specified pixel blurred
                blurred_img_pixel.red = (pixel.red + pixel_b.red + pixel_l.red + pixel_bl.red) // 4
                blurred_img_pixel.green = (pixel.green + pixel_b.green + pixel_l.green + pixel_bl.green) // 4
                blurred_img_pixel.blue = (pixel.blue + pixel_b.blue + pixel_l.blue + pixel_bl.blue) // 4

            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                blurred_img_pixel = blurred_img.get_pixel(x, y)

                # Define the variables of surrounded pixels
                pixel = img.get_pixel(x, y)
                pixel_r = img.get_pixel(x + 1, y)
                pixel_t = img.get_pixel(x, y - 1)
                pixel_tr = img.get_pixel(x + 1, y - 1)

                # Make a specified pixel blurred
                blurred_img_pixel.red = (pixel.red + pixel_t.red + pixel_tr.red + pixel_r.red) // 4
                blurred_img_pixel.green = (pixel.green + pixel_t.green + pixel_tr.green + pixel_r.green) // 4
                blurred_img_pixel.blue = (pixel.blue + pixel_t.blue + pixel_tr.blue + pixel_r.blue) // 4

            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                blurred_img_pixel = blurred_img.get_pixel(x, y)

                # Define the variables of surrounded pixels
                pixel = img.get_pixel(x, y)
                pixel_l = img.get_pixel(x - 1, y)
                pixel_tl = img.get_pixel(x - 1, y - 1)
                pixel_t = img.get_pixel(x, y - 1)

                # Make specified pixel blurred
                blurred_img_pixel.red = (pixel.red + pixel_t.red + pixel_tl.red + pixel_l.red) // 4
                blurred_img_pixel.green = (pixel.green + pixel_t.green + pixel_tl.green + pixel_l.green) // 4
                blurred_img_pixel.blue = (pixel.blue + pixel_t.blue + pixel_tl.blue + pixel_l.blue) // 4

            elif 0 < x < img.width-1 and y == 0:
                # Get top edge's pixels (without two corners)
                blurred_img_pixel = blurred_img.get_pixel(x, y)

                # Define the variables of surrounded pixels
                pixel = img.get_pixel(x, y)
                pixel_l = img.get_pixel(x - 1, y)
                pixel_r = img.get_pixel(x + 1, y)
                pixel_bl = img.get_pixel(x - 1, y + 1)
                pixel_b = img.get_pixel(x, y + 1)
                pixel_br = img.get_pixel(x + 1, y + 1)

                # Make specified pixels blurred
                blurred_img_pixel.red = (pixel.red + pixel_b.red + pixel_bl.red + pixel_l.red + pixel_r.red + pixel_br.red) // 6
                blurred_img_pixel.green = (pixel.green + pixel_b.green + pixel_bl.green + pixel_l.green + pixel_r.green + pixel_br.green) // 6
                blurred_img_pixel.blue = (pixel.blue + pixel_b.blue + pixel_bl.blue + pixel_l.blue + pixel_r.blue + pixel_br.blue) // 6


            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                blurred_img_pixel = blurred_img.get_pixel(x, y)

                # Define the variables of surrounded pixels
                pixel = img.get_pixel(x, y)
                pixel_l = img.get_pixel(x - 1, y)
                pixel_r = img.get_pixel(x + 1, y)
                pixel_tl = img.get_pixel(x - 1, y - 1)
                pixel_t = img.get_pixel(x, y - 1)
                pixel_tr = img.get_pixel(x + 1, y - 1)

                # Make specified pixels blurred
                blurred_img_pixel.red = (pixel.red + pixel_tl.red + pixel_t.red + pixel_tr.red + pixel_r.red + pixel_l.red) // 6
                blurred_img_pixel.green = (pixel.green + pixel_tl.green + pixel_t.green + pixel_tr.green + pixel_r.green + pixel_l.green) // 6
                blurred_img_pixel.blue = (pixel.blue + pixel_tl.blue + pixel_t.blue + pixel_tr.blue + pixel_r.blue + pixel_l.blue) // 6

            elif x == 0 and 0 < y < img.height-1:
                # Get left edge's pixels (without two corners)
                blurred_img_pixel = blurred_img.get_pixel(x, y)

                # Define the variables of surrounded pixels
                pixel = img.get_pixel(x, y)
                pixel_r = img.get_pixel(x + 1, y)
                pixel_t = img.get_pixel(x, y - 1)
                pixel_tr = img.get_pixel(x + 1, y - 1)
                pixel_b = img.get_pixel(x, y + 1)
                pixel_br = img.get_pixel(x + 1, y + 1)

                # Make specified pixels blurred
                blurred_img_pixel.red = (pixel.red + pixel_b.red + pixel_t.red + pixel_tr.red + pixel_r.red + pixel_br.red) // 6
                blurred_img_pixel.green = (pixel.green + pixel_b.green + pixel_t.green + pixel_tr.green + pixel_r.green + pixel_br.green) // 6
                blurred_img_pixel.blue = (pixel.blue + pixel_b.blue + pixel_t.blue + pixel_tr.blue + pixel_r.blue + pixel_br.blue) // 6


            elif x == img.width-1 and 0 < y < img.height-1:
                # Get right edge's pixels (without two corners)
                blurred_img_pixel = blurred_img.get_pixel(x, y)

                # Define the variables of surrounded pixels
                pixel = img.get_pixel(x, y)
                pixel_l = img.get_pixel(x - 1, y)
                pixel_tl = img.get_pixel(x - 1, y - 1)
                pixel_t = img.get_pixel(x, y - 1)
                pixel_bl = img.get_pixel(x - 1, y + 1)
                pixel_b = img.get_pixel(x, y + 1)

                # Make specified pixels blurred
                blurred_img_pixel.red = (pixel.red + pixel_b.red + pixel_t.red + pixel_tl.red + pixel_l.red + pixel_bl.red) // 6
                blurred_img_pixel.green = (pixel.green + pixel_b.green + pixel_t.green + pixel_tl.green + pixel_l.green + pixel_bl.green) // 6
                blurred_img_pixel.blue = (pixel.blue + pixel_b.blue + pixel_t.blue + pixel_tl.blue + pixel_l.blue + pixel_bl.blue)  // 6

            else:
                # Inner pixels.
                blurred_img_pixel = blurred_img.get_pixel(x, y)
                pixel = img.get_pixel(x, y)

                # Define the variables of surrounded pixels
                pixel_l = img.get_pixel(x - 1, y)
                pixel_r = img.get_pixel(x + 1, y)
                pixel_tl = img.get_pixel(x - 1, y - 1)
                pixel_t = img.get_pixel(x, y - 1)
                pixel_tr = img.get_pixel(x + 1, y - 1)
                pixel_bl = img.get_pixel(x - 1, y + 1)
                pixel_b = img.get_pixel(x, y + 1)
                pixel_br = img.get_pixel(x + 1, y + 1)

                sum_red = pixel_br.red + pixel_tr.red + pixel_r.red + pixel.red + pixel_b.red + pixel_t.red + pixel_tl.red + pixel_l.red + pixel_bl.red
                sum_green = pixel_br.green + pixel_tr.green + pixel_r.green + pixel.green + pixel_b.green + pixel_t.green + pixel_tl.green + pixel_l.green + pixel_bl.green
                sum_blue = pixel_br.blue + pixel_tr.blue + pixel_r.blue + pixel.blue + pixel_b.blue + pixel_t.blue + pixel_tl.blue + pixel_l.blue + pixel_bl.blue

                blurred_img_pixel.red = sum_red // 9
                blurred_img_pixel.green = sum_green // 9
                blurred_img_pixel.blue = sum_blue // 9
    return blurred_img


def main():
    """
    This functon blurs the original images through changing
    each pixel in the original image with a predefined algorithm
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()