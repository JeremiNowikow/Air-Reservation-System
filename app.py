from pprint import pprint as pp
class Flight:
    def __init__(self, flight_number, plane):
        self.flight_number = flight_number
        self.plane = plane

        rows, letters = self.plane.get_seating_plan()

        self.seats = [{letter: None for letter in letters} for _ in rows]

    def get_airways(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def get_airplane_model(self):
        return self.plane.get_model()

    def allocate_passenger(self, seat="12C", passenger="Jarosław K."):
        pass



class Airplane:
    def num_seats(self):
        rows, seats = self.get_seating_plan()
        return len(rows) * len(seats)


class Boeing737Max(Airplane):
    @staticmethod
    def get_model():
        return "Boeing 737Max"

    @staticmethod
    def get_seating_plan():
        return range(25), "ABCDEG"

class AirbusA380(Airplane):
    @staticmethod
    def get_model():
        return "Airbus A380"

    @staticmethod
    def get_seating_plan():
        return range(45), "ABCDEGHJK"


boeing = Boeing737Max()
airbus = AirbusA380()
f = Flight("BA324", boeing)
g = Flight("BA324", airbus)

pp(f.seats)