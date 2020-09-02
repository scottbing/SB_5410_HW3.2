from PIL import Image, ImageDraw
from SortFunctions import selectionSort
from SortFunctions import quickSort
from SortFunctions import mergeSort
from SearchFunctions import binarySearchSub

import colorsys


def comparePixels(pix1, pix2):
    return pix1[0][0] > pix2[0][0]


# end def comparePixels(pix1,pix2):


def storePixels(im):
    width = int(im.size[0])
    height = int(im.size[1])

    # store ppixels inout double tuple format.
    pixel_array = []
    yiq_pixels = []

    for i in range(width):  # for loop for x position
        for j in range(height):  # for loop for y position
            # get r and g and b values of pixel at position
            r, g, b = im.getpixel((i, j))
            #yiq conversion is expecting float between 0-1
            yiq = colorsys.rgb_to_yiq(r/255,g/255,b/255)
            yiq_pixels.append([yiq, (i,j)])
            pixel_array.append([(r, g, b), (i, j)])
        # end for j
    # end for i
    return (pixel_array, yiq_pixels) #return both lists in a tuple
# end def storePixels(im):

def pixelsToImage(im, pixels):
    outimg = Image.new("RGB", im.size)
    outimg.putdata([p[0] for p in pixels])
    outimg.show()
    return outimg
# end def pixelsToImage(im, pixels):

def pixelsToPoints(im, pixels):
    #defualt bakground color is black
    #outimg = Image.new("RGB",  size)
    for p in pixels:
        im.putpixel(p[1], p[0])
    im.show()
    #return outimg
# enddef pixelsToPoints(im, pixels):

def grayScale(im, pixels):
    draw = ImageDraw.Draw(im)
    for px in pixels:
        gray_av = int((px[0][0] + px[0][1] + px[0][2])/3)
        draw.point(px[1], (gray_av, gray_av, gray_av))
#end of def grayScale(im, pixels):

def main():
    IMG_NAME = 'tinyrose'

    # open image
    # read each pixel into memory as the image object im
    with Image.open(IMG_NAME + '.jpg') as im:
        pixels,yiq_pixels = storePixels(im)    #store rgb pixels

        print(len(pixels), len(yiq_pixels))     #delete this test

        sorted_pixels = pixels.copy()   #copy pixels fro sorting
        selectionSort(sorted_pixels, comparePixels) #sort on first val
        ## may need sorted image to see what is going on
        #sorted_im = pixelsToImage(im, sorted_pixels)
        #sorted_im.save('sorted_' + IMG_NAME + '.jpg', 'JPEG')

        grayScale(im, pixels)   #grayscale pixels in place
        threshold = 128 #define threshold to throw away pixels after
        subi = binarySearchSub([r[0][0] for r in sorted_pixels],
                               0, len(sorted_pixels)-1, threshold)
        # subi = binarySearchSub([r[0][0] for r in sorted_pixels],
        #                        0, len(sorted_pixels) - 1, threshold)
        pixelsToPoints(im, sorted_pixels[0:subi])  #put saved pixels on gray
        #pixelsToPoints(im, sorted_pixels[subi:])
        im.show()
    # end with Image.open(IMG_NAME + '.jpg') as im:

    # save my image data from memory to a file with a different name
    im.save('highlighted_' + IMG_NAME + '.jpg', 'JPEG')

    # opens with your external preiview program, shows memory representaion
    #im.show()
# end of def main():

if __name__ == "__main__":
    main()
