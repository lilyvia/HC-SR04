#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO


class ultrasonic(object):
    def __init__(self, direction_trigger, direction_echo, mode):
        self.direction_trigger = direction_trigger
        self.direction_echo = direction_echo
        self.mode = mode
        # 设置 GPIO 口的模式
        # set GPIO mode
        GPIO.setmode(self.mode)
        # 定义 GPIO 输入、输出
        # Set GPIO as output and input
        GPIO.setup(self.direction_trigger, GPIO.OUT)
        GPIO.setup(self.direction_echo, GPIO.IN)

    def probe(self):
        # 从 trigger 发射 10us 脉冲
        # Send 10us pulse from trigger
        GPIO.output(self.direction_trigger, 1)
        time.sleep(0.00001)
        GPIO.output(self.direction_trigger, 0)
        start = time.time()

        # Echo 接收脉冲
        # Echo to receive pulse
        while GPIO.input(self.direction_echo) == 0:
            start = time.time()

        while GPIO.input(self.direction_echo) == 1:
            stop = time.time()

        # 计算脉冲长度
        # Calculate pulse length
        elapsed = stop - start
        # 距离 = 时间差 * 声速
        # Distance = time difference * sound velocity
        distance = elapsed * 34300
        # 需要的是单程距离，所以减半
        # Need a one-way distance, so half
        distance = distance / 2
        return distance


# 定义 GPIO 和模式
# Define GPIO and mode
front_trig = 17
front_echo = 27
right_trig = 22
right_echo = 5
left_trig = 23
left_echo = 24
mode_ = GPIO.BCM
front = ultrasonic(front_trig, front_echo, mode_)
right = ultrasonic(right_trig, right_echo, mode_)
left = ultrasonic(left_trig, left_echo, mode_)

# 检查距离
# Check distance
if __name__ == '__main__':
    try:
        while True:
            print("Left_Distance: %.2f cm Front_Distance: %.2f cm Right_Distance: %.2f cm" % (
                left.probe(), front.probe(), right.probe()))
            time.sleep(0.1)
    # 中断时重置GPIO
    # Reset GPIO settings when interrupts
    except KeyboardInterrupt:
        GPIO.cleanup()
    # 结束时重置 GPIO
    # Reset GPIO settings at the end
    finally:
        GPIO.cleanup()
