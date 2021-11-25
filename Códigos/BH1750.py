#!/usr/bin/env python3

"""
Created on Nov 2021

This script read the BH1750 ligh sensor  by I2C bus.

@author: Ingrid Rodríguez and Carlos Rodríguez
"""

import smbus

# Sensor constants
DEVICE     = 0x23 # Default I2C address
POWER_DOWN = 0x00 # Not active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset register
HR_MODE_1  = 0x20 # Mode: 1 resolution: 1 lx

i2c = smbus.SMBus(1)
def convertToNumber(data):
    """
    Convert 2 bytes in a decimal number
    ----------
    data : list
        Data block
    Returns
    -------
    float
        Read luxes 
    """
    result=(data[1] + (256 * data[0])) / 1.2
    return (result)

def readLux(DEVICE):
    """
    Read sensor light values 
    Parameters
    ----------
    DEVICE : int
        Address device

    Returns
    -------
    float
        Ambient light in lux
    """
    data = i2c.read_i2c_block_data(DEVICE,HR_MODE_1,2)
    return convertToNumber(data)
