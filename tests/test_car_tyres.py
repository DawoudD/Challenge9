from lib.car import *
from lib.tyre import *


#when we ask about a certain tyre, the information for only that tyre is given
# i.e FR tyre = this pressure and this thread depth

def test_FR_tyre_information_tyre_pressure():
    car1 = car()
    front_right_tyre = car1.tyres.get("FR")
    front_right_tyre.add_tyre_data(50, 0)
    actual = front_right_tyre.tyre_pressure
    expected = [50]
    assert actual == expected


def test_FR_tyre_information_tread_depth():
    car1 = car()
    front_right_tyre = car1.tyres.get("FR")
    front_right_tyre.add_tyre_data(50, 0)
    actual = front_right_tyre.tread_depth
    expected = [0]
    assert actual == expected


def test_FR_tyre_information_all():
    car1 = car()
    front_right_tyre = car1.tyres.get("FR")
    front_right_tyre.add_tyre_data(50, 0)
    actual = front_right_tyre.all
    expected = [50, 0]
    assert actual == expected