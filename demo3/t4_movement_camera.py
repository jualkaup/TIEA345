#!/usr/bin/env python
# -*- coding: utf-8 -*-

from picamera import PiCamera
from time import sleep
import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

MOVEMENT_SENSOR = 18
CAMERA = PiCamera()

def main():
    GPIO.setup(MOVEMENT_SENSOR, GPIO.IN)
    CAMERA.resolution = (1920, 1080)
    try:
        while True:
            if GPIO.input(MOVEMENT_SENSOR) == 1:
                CAMERA.start_preview()
                sleep(5)
                filename = '/home/pi/dev/demo3/' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '_image.jpg'
                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "- Capturing picture")
                CAMERA.capture(filename)
                CAMERA.stop_preview()
            sleep(0.1)
    except KeyboardInterrupt:
        print "Lopetetaan"


if __name__ == "__main__":
    main()
