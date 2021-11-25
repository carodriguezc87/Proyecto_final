#!/usr/bin/env python3
"""
Created on Nov 2021

This script store data (humidity, temperature, and lux) in a file

@author: Ingrid Rodríguez and Carlos Rodríguez  
"""

import time
import BH1750 as ls
import BME280read as BME280
from datetime import datetime as dt

while True:
    humidity=BME280.readHumidity()
    temperature=BME280.readTemperature()
    light=ls.readLux(0x23)
    now = dt.now()
    timestamp = now.strftime("%d-%m-%Y,%H:%M:%S")
    print("{0}, {1:.2f} %, {2:.2f} °C, {3:.2f} lx\n".format(timestamp,humidity,temperature,light))
    
    file = open("/home/pi/Documents/ProyectoFinal/variables.csv", "a")
    file.write("{0}, {1:.2f} %, {2:.2f} °C, {3:.2f} lx\n".format(timestamp,humidity,temperature,light))
    file.close()
    time.sleep(5)


