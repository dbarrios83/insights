import math

class Camera:
    def __init__(self, id, address, max_speed, latitude, longitude):
        self.id = id
        self.address = address
        self.max_speed = max_speed
        self.latitude = latitude
        self.longitude = longitude

    radius = 6371
    def get_x(self):
        return (self.radius * math.cos(self.latitude) * math.cos(self.longitude))

    def get_y(self):
        return (self.radius * math.cos(self.latitude) * math.sin(self.longitude))

    #x = R * cos(lat) * cos(lon)
    #y = R * cos(lat) * sin(lon)