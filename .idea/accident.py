import math

class Accident:
    def __init__(self, id, latitude, longitude):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude

    radius = 6371
    def get_x(self):
        return (self.radius * math.cos(self.latitude) * math.cos(self.longitude))

    def get_y(self):
        return (self.radius * math.cos(self.latitude) * math.sin(self.longitude))

    #x = R * cos(lat) * cos(lon)
    #y = R * cos(lat) * sin(lon)