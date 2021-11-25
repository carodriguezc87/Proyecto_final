#!/usr/bin/python3
"""
Created on Nov 2021

This script read data from IoT platform switch and turn on-off a LED.

@author: Ingrid Rodríguez and Carlos Rodríguez  
"""

from Adafruit_IO import Client
import wiringpi as wpi

IO_KEY = "Adafruit_KEY"
IO_USERNAME = "Adafruit_USER"

# Client REST instance
aio = Client(IO_USERNAME,IO_KEY)

# Feed setup
led = aio.feeds('hidroponico.led')

output = 0 

# Initialize wiringPi
wpi.wiringPiSetup()

# Define wPi gpio 0 like output mode
wpi.pinMode(output,1)

data = aio.receive(led.key)
if data.value == "ON":
    wpi.digitalWrite(output,1)
elif data.value == "OFF":
    wpi.digitalWrite(output,0)

