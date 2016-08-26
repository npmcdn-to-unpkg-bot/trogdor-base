import serialsensor

class Motor(serialsensor.SerialSensor):
    l_speed = 0
    r_speed = 0
    heading = 0.0

    def __init__(self, port, baud, timeout):
        super().__init__(port, baud, timeout)

    def parse(self):
        reading = self.ser.readline().decode("utf-8").split(',')
        
        if (reading[0] == "speed"):
            self.l_speed = int(reading[1])
            self.r_speed = int(reading[2])
        elif (reading[0] == "compass"):
            self.heading = float(reading[1])

    def get_json(self):
        return {
            "l_speed": self.l_speed,
            "r_speed": self.r_speed,
            "heading": self.heading
        }