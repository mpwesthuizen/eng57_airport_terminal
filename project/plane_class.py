class Plane:
    def __init__(self, aircraft_type, avg_speed, capacity):
        self.aircraft_type = aircraft_type
        self.avg_speed = int(avg_speed)
        self.capacity = int(capacity)

    def get_aircraft_type(self):
        return self.aircraft_type

    def get_avg_speed_kt(self):
        return self.avg_speed

    def get_capacity(self):
        return self.capacity

# plane1 = Plane('Boeing 787-10 Dreamliner', 560, 336)
# print(plane1.aircraft_type)
# print(plane1.avg_speed)
# print(plane1.capacity)