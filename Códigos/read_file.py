#!/usr/bin/python3
"""
Created on Nov 2021

This script read a file and send the data to an IoT platform.

@author: Ingrid Rodríguez and Carlos Rodríguez  
"""

from Adafruit_IO import Client


IO_KEY = "Adafruit_KEY"
IO_USERNAME = "Adafruit_USER"

# Client REST instance
aio = Client(IO_USERNAME,IO_KEY)

# Feeds setup
moisture_feed = aio.feeds('hidroponico.humedad')
temperature_feed = aio.feeds('hidroponico.temperatura')
light_feed = aio.feeds('hidroponico.luminocidad')

# Read file .csv
file = open('/home/pi/Documents/ProyectoFinal/variables.csv','r')
data = file.readlines()[-1]
file.close()

# Extract data
list = data.split(' ')
light = list[1]
humidity= list[3]
temperature = list[5]

#Send data to IoT platform
aio.send(moisture_feed.key, humidity)
aio.send(temperature_feed.key, temperature)
aio.send(light_feed.key, light)
