import serial

class GPS:
    ser = None

    time = None
    latitude = None
    longitude = None
    satellites = 0

    def __init__(self, port, baud, timeout):
        self.ser = serial.Serial(port, baud, timeout=timeout)

    def parse_time(rmc_data):
        time = rmc_data[1]
        hours = time[0:2]
        minutes = time[2:4]
        seconds = time[4:6]
        return hours + ":" + minutes + ":" + seconds

    def parse_latitude(rmc_data):
        return 40

    def parse_longitude(rmc_data):
        return -80

    def parse_rmc(self, rmc_data):
        self.time = parse_time(rmc_data)
        self.latitude = parse_latitude(rmc_data)
        self.longitude = parse_latitude(rmc_data)

    def parse(self):
        reading = self.ser.readline().decode("utf-8").split(',')
        if (reading[0] == "$GPRMC"):
            self.parse_rmc(reading)

    def get_json(self):
        return {'time': self.time, 'latitude': self.latitude, 'longitude': self.longitude}