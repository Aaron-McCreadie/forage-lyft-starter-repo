from ..interfaces.tires import Tires


class OctoprimeTires(Tires):

    def __init__(self, tire_wear_values):
        self.tire_wear_values = tire_wear_values

    def needs_service(self) -> bool:
        return sum(self.tire_wear_values) >= 3
