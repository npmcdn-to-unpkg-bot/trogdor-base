# Read GPS data from serial and parse it into something useful

import serial

def time(time):
    hours = time[0:2]
    minutes = time[2:4]
    seconds = time[4:6]
    return hours + ":" + minutes + ":" + seconds

def latitude(latitude):
    degrees = latitude[0:2]
    minutes = latitude[2:4]
    seconds = latitude[5:7] + "." + latitude[7:]
    return degrees + " " + minutes + "' " + seconds + '"'

def longitude(longitude):
    degrees = longitude[0:3]
    minutes = longitude[3:5]
    seconds = longitude[6:8] + "." + longitude[8:]
    return degrees + " " + minutes + "' " + seconds + '"'

def main():
    port = "/dev/ttyUSB0"
    baud = 9600
    timeout = 10

    ser = serial.Serial(port, baud, timeout=timeout)

    while True:
        reading = ser.readline().split(",")

        if (reading[0] == "$GPRMC"):
            t = reading[1]
            lat = reading[3]
            lon = reading[5]

            print("Time: " + time(t))
            print("Lat: " + latitude(lat))
            print("Longitude: " + longitude(lon))

    ser.close()

main()