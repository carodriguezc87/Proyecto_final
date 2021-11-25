#!/usr/bin/env python3

"""
Created on Nov 2021

This script read temperature and humidity from BME280 sensor by I2C bus.

@author: Ingrid Rodríguez and Carlos Rodríguez
"""

import smbus2
import bme280

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address, calibration_params)

def readTemperature():
        data = bme280.sample(bus, address, calibration_params)
        return data.temperature


def readPressure():
        data = bme280.sample(bus, address, calibration_params)
        return data.pressure


def readHumidity():
        data = bme280.sample(bus, address, calibration_params)
        return data.humidity

