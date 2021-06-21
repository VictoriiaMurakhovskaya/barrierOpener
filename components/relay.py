##################################################

#           P26 ----> Relay_Ch1
#			P20 ----> Relay_Ch2
#			P21 ----> Relay_Ch3

##################################################
# !/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

Relay_Ch1 = 23
relays = [24, 25, 1, 12]


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay_Ch1, GPIO.OUT)
for item in relays:
    GPIO.setup(item, GPIO.OUT)



print("Setup The Relay Module is [success]")

try:
    while True:
        # Control the Channel 1
        GPIO.output(Relay_Ch1, GPIO.LOW)
        print("Channel 1:The Common Contact is access to the Normal Open Contact!")
        time.sleep(1.5)

        for item in relays:
            GPIO.output(item, GPIO.LOW)

        GPIO.output(Relay_Ch1, GPIO.HIGH)
        print("Channel 1:The Common Contact is access to the Normal Closed Contact!\n")
        time.sleep(1.5)

        for item in relays:
            GPIO.output(item, GPIO.HIGH)


except:
    print("except")
    GPIO.cleanup()