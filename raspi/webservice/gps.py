import serial

class GPS:
    ser = None

    time = None
    latitude = None
    longitude = None
    satellites = 0

    def __init__(self, port, baud, timeout):
        self.ser = serial.Serial(port, baud, timeout=timeout)

    def parse_time(self, rmc_data):
        time = rmc_data[1]
        hours = time[0:2]
        minutes = time[2:4]
        seconds = time[4:6]
        return hours + ":" + minutes + ":" + seconds

    def parse_latitude(self, rmc_data):
        latitude = rmc_data[3]
        degrees = float(latitude[:2])
        minutes = float(latitude[2:])
        decimal = degrees + minutes / 60

        return decimal

    def parse_longitude(self, rmc_data):
        longitude = rmc_data[5]
        degrees = float(longitude[:3])
        minutes = float(longitude[3:])
        decimal = degrees + minutes / 60

        if rmc_data[6] == "W":
            decimal *= -1

        return decimal

    def parse_rmc(self, rmc_data):
        self.time = self.parse_time(rmc_data)
        self.latitude = self.parse_latitude(rmc_data)
        self.longitude = self.parse_longitude(rmc_data)

    def parse(self):
        reading = self.ser.readline().decode("utf-8").split(',')
        if (reading[0] == "$GPRMC"):
            self.parse_rmc(reading)

    def get_json(self):
        return {'time': self.time, 'latitude': self.latitude, 'longitude': self.longitude}