from pprint import pprint as pp

from flight import Flight
from planes.airbus_a380 import AirbusA380
from planes.boeing737max import Boeing737Max


def make_flight():
    boeing = Boeing737Max()
    airbus = AirbusA380()
    f = Flight("BA324", boeing)
    g = Flight("BA324", airbus)


    f.allocate_passenger("1C", "Jarosław K")
    f.allocate_passenger("12E", "Paweł K")
    f.allocate_passenger("12A", "Lech K")
    pp(f.seats)
    print(f.plane.num_seats())
    print(f.get_num_empty_seats())
