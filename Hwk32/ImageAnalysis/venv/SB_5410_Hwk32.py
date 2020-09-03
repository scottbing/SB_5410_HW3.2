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

    #list element 0, tuple value 0, inner tuple value 0
    if type(pixels[0][0][0]) == float:  #dealing with YIQ
        print("yiq")
        yiq_out = []
        for p in pixels:
            r,g,b = colorsys.yiq_to_rgb(p[0][0], p[0][1], p[0][2])
            #rgb comes out of conversion as 0-1 float
            r,g,b = int(r*255), int(g*255), int(b*255)
            yiq_out.append((r,g,b))
        outimg.putdata(yiq_out)
        #end for p in pixels:
    else:   #dealing with RGB
        outimg.putdata([p[0] for p in pixels])
    #outimg.show()
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

        selectionSort(yiq_pixels, comparePixels) #sort on first val
        ## may need sorted image to see what is going on
        sorted_im = pixelsToImage(im, yiq_pixels)
        sorted_im.save('sorted_' + IMG_NAME + '.jpg', 'JPEG')

        grayScale(im, pixels)   #grayscale pixels in place
        #replace threshold with target color to pivot around
        target = (183/255, 198/255, 144/255)    # /255 for conversion
        yiq_target = colorsys.rgb_to_yiq(target[0], target[1], target[2])

        #use yiq_target instead  of threshold in search
        subi = binarySearchSub([r[0][0] for r in yiq_pixels],
                               0, len(yiq_pixels)-1, yiq_target[0])
        print(subi)
        # subi = binarySearchSub([r[0][0] for r in sorted_pixels],
        #                        0, len(sorted_pixels) - 1, threshold)
        pixelsToPoints(im, yiq_pixels[0:subi])  #put saved pixels on gray
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
