#!/usr/bin/python

import os.path
import sys
import numpy
import matplotlib.image

version = "0.1"

pixel_size_mm = 0.4
half_pixel_size_mm = pixel_size_mm * 0.5
quarter_pixel_size_mm = pixel_size_mm * 0.25
fifth_pixel_size_mm = pixel_size_mm * 0.2

pen_up_gcode = "M8\n"
pen_down_gcode = "M9\n"
initial_gcode = f'G21\nG91\nG92 X0 Y0 Z0\nF2000\nG01 X0 Y{str(half_pixel_size_mm)} Z0\n'
final_gcode = "G28\n"

pen_up = False
backwards = False

def penUp(pen_up):
    gcode = ""
    if not pen_up:
        gcode = pen_up_gcode
        pen_up = True
    return gcode

def penDown(pen_up):
    gcode = ""
    if pen_up:
        gcode = pen_down_gcode
        pen_up = False
    return gcode

def advanceY(backwards):
    gcode = penUp(pen_up)
    gcode += f'G01 X0 Y{str(pixel_size_mm)} Z0\n'
    backwards = not backwards
    return gcode

def advanceX(backwards, x_mm):
    gcode = " X"
    if backwards:
        gcode += "-"
    gcode += str(x_mm)
    return gcode

def drawSpace(backwards):
    gcode = penUp(pen_up)
    gcode += "G00"
    gcode += advanceX(pixel_size_mm)
    gcode += " Y0 Z0\n"
    return gcode

def drawPixel(backwards):
    gcode = penDown(pen_up)
    gcode += "G01"
    gcode += advanceX(backwards, pixel_size_mm)
    gcode += " Y0 Z0\n"
    return gcode

def processPixel(pixel):
    value = pixel[0]
    if value > 0.90:
        gcode = drawSpace(backwards)
    else:
        gcode = drawPixel(backwards)
    return gcode

def help():
    print(" Command: python imagetogcode.py image_filename [output_filename]\n")

def main():
    argc = len(sys.argv)
    print("Image to G-Code v" + version)

    if argc < 2:
        help()
        sys.exit(2)

    image_filename = sys.argv[1]
    if not os.path.exists(image_filename):
        print("File not found: " + image_filename)
        sys.exit(1)

    print("Reading image file: " + image_filename)
    img = matplotlib.image.imread(image_filename)
    height = len(img)
    width = len(img[0])
    channels = len(img[0][0])
    print("Width: " + str(width) + ", Height: " + str(height) + ", Channels: " + str(channels))

    # Initialise G-Code
    gcode = initial_gcode
    gcode += penUp(pen_up)

    # Plot image
    reverse = False
    for y in range(height - 1, 0, -1):
        if reverse:
            for x in range(width - 1, -1, -1):
                gcode += processPixel(img[y][x])
        else:
            for x in range(width):
                gcode += processPixel(img[y][x])
        gcode += advanceY(backwards)
        reverse = not reverse

    # Finalise G-Code
    gcode += penUp(pen_up)
    gcode += final_gcode

    if argc > 2:
        output_filename = sys.argv[2]
        file = open(output_filename, "w+")
        print("Writing GCode to: " + output_filename)
        file.write(gcode)
        file.close()
    else:
        print(gcode)


if __name__ == "__main__":
    main()
