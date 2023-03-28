from planes.airplane import Airplane


class Boeing737Max(Airplane):
    @staticmethod
    def get_model():
        return "Boeing 737Max"

    @staticmethod
    def get_seating_plan():
        return range(25), "ABCDEG"
