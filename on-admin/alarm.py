#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

for a in range (5) :
	GPIO.output(3,1)
	time.sleep(1)
	GPIO.output(3,0)
	time.sleep(1)
	GPIO.output(5,1)
	time.sleep(1)
	GPIO.output(5,0)
	time.sleep(1)
	GPIO.output(7,1)
	time.sleep(1)
	GPIO.output(7,0)
