#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

CAR_RED_LED_PIN = 4
CAR_YELLOW_LED_PIN = 5
CAR_GREEN_LED_PIN = 6

PED_GREEN_LED_PIN = 20
PED_YELLOW_LED_PIN = 16
PED_RED_LED_PIN = 21

PED_BUTTON = 26

MOVEMENT_SENSOR = 12

def main():
    # Alustetaan ledien/namiskan/liikesensorin pinit
    init()

    # Laitetaan raspi pyörittämään ikuista silmukkaa joka katkaistaan komennolla CTRL+C
    try:
        # Normaalitilanne: autoille palaa vihreä, jalankulkijoille punainen
        default_lights()
        while True:
            # Nappia painamalla vaihdetaan jalankulkijoille vihreät valot
            if GPIO.input(PED_BUTTON) == 1:
                button_push()
                # Jonka jälkeen vaihdetaan autoilijoille vihreät valot
                default_lights()
            sleep(0.1)
    except KeyboardInterrupt:
        print "Lopetetaan"

    GPIO.cleanup()

def default_lights():
    GPIO.output(PED_GREEN_LED_PIN, 0)
    GPIO.output(PED_RED_LED_PIN, 1)

    GPIO.output(CAR_GREEN_LED_PIN, 0)
    GPIO.output(CAR_RED_LED_PIN, 1)
    sleep(1)
    GPIO.output(CAR_YELLOW_LED_PIN, 1)
    sleep(1)
    GPIO.output(CAR_RED_LED_PIN, 0)
    GPIO.output(CAR_YELLOW_LED_PIN, 0)
    GPIO.output(CAR_GREEN_LED_PIN, 1)

def button_push():
    GPIO.output(PED_YELLOW_LED_PIN, 1)

    # Jos havaitaan liikettä, odotetaan 5 sekuntia ennenkuin vaihdetaan jalankulkijoille vihreät
    if GPIO.input(MOVEMENT_SENSOR) == 1:
        sleep(5)

    GPIO.output(CAR_GREEN_LED_PIN, 0)
    GPIO.output(CAR_YELLOW_LED_PIN, 1)
    sleep(1)
    GPIO.output(CAR_YELLOW_LED_PIN, 0)
    GPIO.output(CAR_RED_LED_PIN, 1)
    sleep(1)
    GPIO.output(PED_RED_LED_PIN, 0)
    GPIO.output(PED_YELLOW_LED_PIN, 0)
    GPIO.output(PED_GREEN_LED_PIN, 1)
    sleep(8)
    GPIO.output(PED_GREEN_LED_PIN, 0)
    sleep(0.5)
    GPIO.output(PED_GREEN_LED_PIN, 1)
    sleep(0.5)
    GPIO.output(PED_GREEN_LED_PIN, 0)
    sleep(0.5)
    GPIO.output(PED_GREEN_LED_PIN, 1)
    sleep(0.5)


def init():
    GPIO.setup(CAR_RED_LED_PIN, GPIO.OUT)
    GPIO.setup(CAR_YELLOW_LED_PIN, GPIO.OUT)
    GPIO.setup(CAR_GREEN_LED_PIN, GPIO.OUT)
    GPIO.setup(PED_GREEN_LED_PIN, GPIO.OUT)
    GPIO.setup(PED_YELLOW_LED_PIN, GPIO.OUT)
    GPIO.setup(PED_RED_LED_PIN, GPIO.OUT)
    GPIO.setup(PED_BUTTON, GPIO.IN)
    GPIO.setup(MOVEMENT_SENSOR, GPIO.IN)

if __name__ == "__main__":
    main()
