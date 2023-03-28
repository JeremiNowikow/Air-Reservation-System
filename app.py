from pprint import pprint as pp

class Flight:
    def __init__(self, flight_number, plane):
        self.flight_number = flight_number
        self.plane = plane

        rows, letters = self.plane.get_seating_plan()

        self.seats = [None] + [{letter: None for letter in letters} for _ in rows]

    def get_airways(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def get_airplane_model(self):
        return self.plane.get_model()

    def _parse_seat(self, seat="12C"):
        rows, letters = self.plane.get_seating_plan()
        letter = seat[-1]

        if letter not in letters:
            raise ValueError(f"Invalid seat letter: {letter}")
        row_text = seat[:-1]

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid row digit: {row_text}")

        if row not in rows:
            raise ValueError(f"Row is out of airplane range: {row}")

        return row, letter

    def allocate_passenger(self, seat, passenger):
        row, letter = self._parse_seat(seat)

        if self.seats[row][letter] is not None:
            raise ValueError(f"Seat is already occupied: {seat}")
        self.seats[row][letter] = passenger

    def get_num_empty_seats(self):
        # empty_seats = 0
        # for row in self.seats:
        #     if row is not None:
        #         for passenger in row.values():
        #             if passenger is None:
        #                 empty_seats += 1
        #
        # return empty_seats

        return sum(sum(1 for passenger in row.values() if passenger is None) for row in self.seats if row is not None)




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


f.allocate_passenger("1C", "Jarosław K")
f.allocate_passenger("12E", "Paweł K")
f.allocate_passenger("12A", "Lech K")
pp(f.seats)
print(f.plane.num_seats())
print(f.get_num_empty_seats())
