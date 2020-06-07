from project.terminal  import *
# Todo: add a delete flight, airport assistant login credentials, enforce max capacity on passenger list.

class Flight(Terminal):
    instances = []

    def __init__(self, flight, departure, destination, flight_date, flight_time, plane, capacity, flight_list=None):
        self.flight = flight.capitalize()
        self.departure = int(departure)
        Flight.instances.append(self.flight)
        self.destination = destination.capitalize()
        self.flight_date = flight_date
        self.flight_time = flight_time
        self.plane = plane.capitalize()
        self.capacity = capacity
        self.flight_list = flight_list
        if flight_list is None:
            self.flight_list = []

    def delay(self, new_time):
        self.departure = new_time

    def divert(self, new_destination):
        self.destination = new_destination

    def alter_aircraft(self, new_plane):
        self.plane = new_plane

    def show_report(self):
        report = vars(self)
        for key, value in report.items():
            print(key.capitalize(), ": ", value)

    def append_flight_list(self, passenger):
        self.flight_list.append(passenger)

    def show_flight_list(self):
        print(f"\nFlight list for personnel on flight {self.flight}: ")
        for person in self.flight_list:
            print(vars(person))