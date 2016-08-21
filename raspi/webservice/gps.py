# Read GPS data from serial and parse it into something useful

import serial

# Return formatted time from RMC message
def time(rmc):
    time = rmc[1]
    hours = time[0:2]
    minutes = time[2:4]
    seconds = time[4:6]
    return hours + ":" + minutes + ":" + seconds

# Return decimal coordinates from RMC message
def latitude(rmc):
    latitude = rmc[3]
    degrees = float(latitude[0:2])
    minutes = float(latitude[2:4]) / 60
    seconds = latitude[5:7]
    seconds_decimal = '.' + latitude[7:]
    seconds_total = (float(seconds) + float(seconds_decimal)) / 3600
    return degrees + minutes + seconds_total

# Return decimal coordinates from RMC message
def longitude(rmc):
    longitude = rmc[5]
    degrees = float(longitude[0:3])
    minutes = float(longitude[3:5]) / 60

    seconds = longitude[6:8]
    seconds_decimal = '.' + longitude[8:]
    seconds_total = (float(seconds) + float(seconds_decimal)) / 3600

    return -(degrees + minutes + seconds_total)

# Return number of satellites in view from GSV data
def satellites(gsv):
    return gsv[3]
