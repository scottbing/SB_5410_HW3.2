from PIL import Image, ImageDraw
from SortFunctions import selectionSort
from SortFunctions import quickSort
from SortFunctions import mergeSort
from SearchFunctions import binarySearchSub
from PixelFunctions import *
import colorsys
import os

TOGGLE_SLICE = False
TOLERENCE = False
RED = 183
GREEN = 198
BLUE = 144

#Check for numeric and 0-255
#https://stackoverflow.com/questions/31684083/validate-if-input-string-is-a-number-between-0-255-using-regex
def is_number(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def main():
    global TOGGLE_SLICE
    global RED
    global GREEN
    global BLUE
    global TOLERENCE

    while (True):

        IMG_NAME = 'tinyrose'   #tiny rose
        #IMG_NAME = 'bigrose'   #big rose

        # open image
        # read each pixel into memory as the image object im
        with Image.open(IMG_NAME + '.jpg') as im:
            pixels, yiq_pixels = storePixels(im)  # store rgb pixels

            # selectionSort(yiq_pixels, comparePixels) #sort on first val
            mergeSort(yiq_pixels, comparePixels)  # sort on first val
            ## may need sorted image to see what is going on
            sorted_im = pixelsToImage(im, yiq_pixels)
            sorted_im.save('sorted_' + IMG_NAME + '.jpg', 'JPEG')

            grayScale(im, pixels)  # grayscale pixels in place
            # replace threshold with target color to pivot around
            target = (int(RED) / 255, int(GREEN) / 255, int(BLUE) / 255)  # /255 for conversiono
            print("RED: ", RED)
            print("GREEN: ", GREEN)
            print("BLUE: ", BLUE)
            yiq_target = colorsys.rgb_to_yiq(target[0], target[1], target[2])

            if TOLERENCE:
                tolerance = int(len(yiq_pixels)/2)
                print("Tolerance: ", tolerance)
                # change the pivot point
                subi = tolerance
                TOLERENCE = False   #reset tolerance
            else:
                # use yiq_target instead  of threshold in search
                subi = binarySearchSub([r[0][0] for r in yiq_pixels],
                                        0, len(yiq_pixels) - 1, yiq_target[0])

            print("subi:", subi)
            # subi = binarySearchSub([r[0][0] for r in sorted_pixels],
            #                        0, len(sorted_pixels) - 1, threshold)
            if (TOGGLE_SLICE):
                pixelsToPoints(im, yiq_pixels[0:subi])  # put saved pixels on gray
            else:
                pixelsToPoints(im, yiq_pixels[subi:])
            im.show()
        # end with Image.open(IMG_NAME + '.jpg') as im:

        # command = input("Type (Q|q) to save file and quit:")
        # if (command in ('q', 'Q')):
        #     # save my image data from memory to a file with a different name
        #     im.save('highlighted_' + IMG_NAME + '.jpg', 'JPEG')
        #     break

        #taken from: https://stackoverflow.com/questions/34192588/simple-menu-in-python-3
        choice = '0'
        while choice == '0':
            print("Main Choice: Choose 1 of 5 choices")
            print("Choose '(Q|q)' to save file and quit:")
            print("Choose '(R|r)' to reverse the image")
            print("Choose '(T|t)' to set image Tolerance")
            print("Choose '(C|c)' to set image's RGB value")

            choice = input("Please make a choice: ")
            if choice in ('q', 'Q'):
                # save my image data from memory to a file with a different name
                im.save('highlighted_' + IMG_NAME + '.jpg', 'JPEG')
                quit()
            elif choice in ('r', 'R'):
                TOGGLE_SLICE = not TOGGLE_SLICE     # toggle
                print("Do 'R'")
            elif choice in ('t', 'T'):
                TOLERENCE = True
            elif choice in ('c', 'C'):
                r = input("Enter a value for red: ")
                if is_number(r):
                    RED = r
                else:
                    print("Invalid value for Red")
                g = input("Enter a value for green: ")
                if is_number(g):
                    GREEN = g
                else:
                    print("Invalid value for Green")
                b = input("Enter a value for blue: ")
                if is_number(b):
                    BLUE = b
                else:
                    print("Invalid value for Blue")
            else:
                print("I don't understand your choice.")

    # opens with your external preiview program, shows memory representaion
    # im.show()


# end of def main():

if __name__ == "__main__":
    main()
