#!/usr/bin/env python

import time
import RPi.GPIO as GPIO


class ultrasonic(object):
    def __init__(self, direction_trigger, direction_echo, mode):
        self.direction_trigger = direction_trigger
        self.direction_echo = direction_echo
        self.mode = mode
        GPIO.setmode(self.mode)
        GPIO.setup(self.direction_trigger, GPIO.OUT)
        GPIO.setup(self.direction_echo, GPIO.IN)

    def probe(self):
        GPIO.output(self.direction_trigger, 1)
        time.sleep(0.00001)
        GPIO.output(self.direction_trigger, 0)
        start = time.time()

        while GPIO.input(self.direction_echo) == 0:
            start = time.time()

        while GPIO.input(self.direction_echo) == 1:
            stop = time.time()

        elapsed = stop - start
        distance = elapsed * 34300
        distance = distance / 2
        return distance


front_trig =
front_echo =
right_trig =
right_echo =
left_trig =
left_echo =
mode_ =
front = ultrasonic(front_trig, front_echo, mode_)
right = ultrasonic(right_trig, right_echo, mode_)
left = ultrasonic(left_trig, left_echo, mode_)
