#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Adafruit_DHT
from time import sleep
from datetime import datetime

SENSOR = Adafruit_DHT.DHT11
SENSOR_PIN = 5

def main():
    try:
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(SENSOR, SENSOR_PIN)
            if humidity is not None and temperature is not None:
                print(datetime.now())
                print(' Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
            else:
                print(datetime.now())
                print(' Failed to get a reading.')
            sleep(5)
    except KeyboardInterrupt:
        print "Lopetetaan"

if __name__ == "__main__":
    main()
