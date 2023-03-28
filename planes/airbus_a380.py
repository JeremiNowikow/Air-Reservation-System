from planes.airplane import Airplane


class AirbusA380(Airplane):
    @staticmethod
    def get_model():
        return "Airbus A380"

    @staticmethod
    def get_seating_plan():
        return range(45), "ABCDEGHJK"
