# Read GPS data from serial and parse it into something useful

import serial

# Return formatted time from RMC message
def time(rmc):
    time = rmc[1]
    hours = time[0:2]
    minutes = time[2:4]
    seconds = time[4:6]
    return hours + ":" + minutes + ":" + seconds

# Return formatted latitude from RMC message
def latitude(rmc):
    latitude = rmc[3]
    degrees = latitude[0:2]
    minutes = latitude[2:4]
    seconds = latitude[5:7] + "." + latitude[7:]
    return degrees + " " + minutes + "' " + seconds + '"'

# Return formatted longitude from RMC message
def longitude(rmc):
    longitude = rmc[5]
    degrees = longitude[0:3]
    minutes = longitude[3:5]
    seconds = longitude[6:8] + "." + longitude[8:]
    return degrees + " " + minutes + "' " + seconds + '"'

# Return number of satellites in view from GSV data
def satellites(gsv):
    return gsv[3]

def main():
    port = "/dev/ttyUSB0"
    baud = 9600
    timeout = 10

    ser = serial.Serial(port, baud, timeout=timeout)

    while True:
        reading = ser.readline().split(",")

        if (reading[0] == "$GPRMC"):
            print("Time: " + time(reading))
            print("Lat: " + latitude(reading))
            print("Longitude: " + longitude(reading))

        elif (reading[0] == "$GPGSV"):
            if (int(reading[2]) == 1):   # Sentence number has to be 1
                print("Satellites: " + satellites(reading))

    ser.close()

main()