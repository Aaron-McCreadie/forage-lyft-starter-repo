from ..interfaces.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tire_wear_values):
        self.tire_wear_values = tire_wear_values

    def needs_service(self) -> bool:
        return any(value >= 0.9 for value in self.tire_wear_values)
