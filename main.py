#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-18 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
An analog clockface with date & time.
Ported from:
https://gist.github.com/TheRayTracer/dd12c498e3ecb9b8b47f#file-clock-py
"""

import math
import time
import datetime
import pygame
from pygame.locals import *
from demo_opts import get_device
from luma.core.render import canvas
from PIL import ImageFont


def posn(angle, arm_length):
    dx = int(math.cos(math.radians(angle)) * arm_length)
    dy = int(math.sin(math.radians(angle)) * arm_length)
    return (dx, dy)

font = ImageFont.truetype("fonts/Dot Matrix Regular.ttf", 12)
fontBold = ImageFont.truetype("fonts/Dot Matrix Bold.ttf", 12)
fontBoldTall = ImageFont.truetype("fonts/Dot Matrix Bold Tall.ttf", 12)
fontBoldLarge = ImageFont.truetype("fonts/Dot Matrix Bold.ttf", 20)

pygame.init()
print("Test")

max_line = 4

def main():
    today_last_time = "Unknown"
    sel_line = 0
    while True:
        now = datetime.datetime.now()
        today_date = now.strftime("%d %b %y")
        today_time = now.strftime("%H:%M:%S")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_p]:
            sel_line += 1

        if sel_line >= max_line:
            sel_line = 0
        
        if today_time != today_last_time:
            today_last_time = today_time
            with canvas(device) as draw:
                now = datetime.datetime.now()
                #today_date = now.strftime("%d %b %y")
                line = 0

                cx = 0
                cxr = 256
                cy = 0
                lh = 11 # line height

                draw.rectangle((cx, cy, cxr, cy + lh*(sel_line+1)-1), outline="white", fill="white")
                draw.rectangle((cx, cy, cxr, cy + lh*(sel_line)-1), outline="black", fill="black") # Clean up previously selected line

                draw.text((cx, cy + lh*line), "19:49 Augsburg Hbf", fill = "black" if line == sel_line else "white", font=font)
                draw.text((cxr, cy + lh*line), "1    20:15", fill = "black" if line == sel_line else "white", font=font, anchor="rt")

                line += 1
                draw.text((cx, cy + lh*line), "20:10 Landsberg (Lech)", fill = "black" if line == sel_line else "white", font=font)
                draw.text((cxr, cy + lh*line), "2   20:20", fill = "black" if line == sel_line else "white", font=font, anchor="rt")

                line += 1
                draw.text((cx, cy + lh*line), "20:20 Augsburg Hbf", fill = "black" if line == sel_line else "white", font=font)
                draw.text((cxr, cy + lh*line), "1   20:25", fill = "black" if line == sel_line else "white", font=font, anchor="rt")

                line += 1
                draw.text((cx, cy + lh*line), "20:40 Landsberg (Lech)", fill = "black" if line == sel_line else "white", font=font)
                draw.text((cxr, cy + lh*line), "2   20:40", fill = "black" if line == sel_line else "white", font=font, anchor="rt")

        time.sleep(0.1)


if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass