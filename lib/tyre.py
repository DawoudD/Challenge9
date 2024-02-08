# from lib.car import *

class tyre:
    def __init__(self):
        self.tyre_pressure = []
        self.tread_depth = []
        self.all = []
        self.readings = {
            'latest': '',
            'historical_readings': {
                "date": "reading", 
                "date": "reading"
            }
        }

    def add_tyre_data(self, tyre_pressure, tread_depth):
        self.tyre_pressure.append(tyre_pressure)
        self.tread_depth.append(tread_depth)
        self.all.append(tyre_pressure)
        self.all.append(tread_depth)

    def add_historical_data():
        pass
