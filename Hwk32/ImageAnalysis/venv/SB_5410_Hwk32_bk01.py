from PIL import Image, ImageDraw
from SortFunctions import selectionSort
from SortFunctions import quickSort
from SearchFunctions import binarySearchSub


def comparePixels(pix1, pix2):
    return pix1[0][0] > pix2[0][0]


# end def comparePixels(pix1,pix2):


def storePixels(im):
    width = int(im.size[0])
    height = int(im.size[1])

    # store ppixels inout double tuple format.
    pixel_array = []

    for i in range(width):  # for loop for x position
        for j in range(height):  # for loop for y position
            # get r and g and b values of pixel at position
            r, g, b = im.getpixel((i, j))
            pixel_array.append([(r, g, b), (i, j)])
        # end for j
    # end for i
    return pixel_array
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
        pixels = storePixels(im)
        print("stored")

        ### sort copy of pixels ###
        sorted_pixels = pixels.copy()
        #selectionSort(sorted_pixels, comparePixels)
        quickSort(sorted_pixels, 0, len(sorted_pixels)-1, comparePixels)
        print("sorted")
        sorted_im = pixelsToImage(im, sorted_pixels)
        sorted_im.save('sorted_'+ IMG_NAME + '.jpg', 'JPEG')

        # grayscale pixels in place
        #grayScale(im, pixels)

        while(True): #do whileloop in Python does not exist
            command = input("Type a value for red threshold or Q to quit:")
            if command in ('q', 'Q'):
                save = input("Save File? (Y|y) or any key to Quit")
                if save in ('y', 'Y'):
                    format = input("which format?  enter '1' for 'JPEG';  '2' for 'PNG'")
                    if format == '1':
                        print("JPEG")
                        im.save('highlighted_' + IMG_NAME + '.jpg', 'JPEG')
                    elif format == '2':
                        print("PNG")
                        im.save('highlighted_' + IMG_NAME + '.png', 'PNG')
                    else:
                        print("Invalid option - file was not saved")
                break   #leave loop

            #might want to test that command is a number or convert it
            threshold = int(command)

            # grayscale pixels in place
            grayScale(im, pixels)

            #search copy for r
            # use a comprehension to find the sorted r values
            # sorted_r_values = [r[0][0] for r in sorted_pixels}
            subi = binarySearchSub([r[0][0] for r in sorted_pixels],
                                   0, len(sorted_pixels)-1, threshold)
            #print("Sublist of resds starts at: ", subi)

            # restore found r
            # uses list slice notation to remove any item before subi
            pixelsToPoints(im, sorted_pixels[subi:])
            #pixelsToPoints(im, sorted_pixels[0:subi])
            im.show()
        #end while(True)

    # end with Image.open(IMG_NAME + '.jpg') as im:

    # save my image data from memory to a file with a different name
    im.save('highlighted_' + IMG_NAME + '.jpg', 'JPEG')

    # opens with your external preiview program, shows memory representaion
    #im.show()
# end of def main():

if __name__ == "__main__":
    main()
