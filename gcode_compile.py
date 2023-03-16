#!/usr/bin/python

import os.path
import sys
from PIL import Image

pixel_size_mm = 0.4
PEN_UP = "M8\n"
PEN_DOWN = "M9\n"
START = f'G21\nG91\nG92 X0 Y0 Z0\nF2000\nG01 X0 Y{str(pixel_size_mm/2)} Z0\n'
END = "G28\n"

class GcodeCompiler():
    def __init__(self, version=0.1, pixel_size_mm=pixel_size_mm, pen_up_instr=PEN_UP, pen_down_instr=PEN_DOWN, startup_instr=START, end_instr=END, pen_up_state=False, backwards=False):
        self.version = version
        self.pixel_size_mm = pixel_size_mm
        self.pen_up_instr = pen_up_instr
        self.pen_down_instr = pen_down_instr
        self.startup_instr = startup_instr
        self.end_instr = end_instr
        self.pen_up_state = pen_up_state
        self.backwards = backwards

    def pen_up(self):
        gcode = ""
        if not self.pen_up_state:
            gcode = pen_up_instr
            self.pen_up_state = True
        return gcode

    def pen_down(self):
        gcode = ""
        if self.pen_up_state:
            gcode = pen_down_instr
            self.pen_up_state = False
        return gcode

    def advance_y(self):
        gcode = f'{self.penUp(self)}G01 X0 Y{str(self.pixel_size_mm)} Z0\n'
        self.backwards = not self.backwards
        return gcode

    def advance_x(self, x_mm):
        gcode = " X"
        if self.backwards:
            gcode += "-"
        gcode += str(x_mm)
        return gcode

    def draw_space(self):
        return f'{self.penUp(self)}G00{self.advanceX(self)} Y0 Z0\n'

    def processPixel():
