class Airplane:
    def num_seats(self):
        rows, seats = self.get_seating_plan()
        return len(rows) * len(seats)
