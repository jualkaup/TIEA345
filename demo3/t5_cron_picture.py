#!/usr/bin/env python
# -*- coding: utf-8 -*-

from picamera import PiCamera
from time import sleep
import datetime

CAMERA = PiCamera()

def main():
    CAMERA.start_preview()
    sleep(5)
    filename = '/home/pi/dev/demo3/' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '_image.jpg'
    CAMERA.capture(filename)
    CAMERA.stop_preview()

if __name__ == "__main__":
    main()