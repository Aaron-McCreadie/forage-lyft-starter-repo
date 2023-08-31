from datetime import date
from typing import List

from car import Car
from battery import SpindlerBattery, NubbinBattery
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from tires import CarriganTires, OctoprimeTires


class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int, tire_wear_values: List[float]) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear_values)
        return Car(engine, battery, tires)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int, tire_wear_values: List[float]) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear_values)
        return Car(engine, battery, tires)

    @staticmethod
    def create_pailndrome(current_date: date, last_service_date: date, warning_light_on: bool,
                          tire_wear_values: List[float]) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTires(tire_wear_values)
        return Car(engine, battery, tires)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int,
                         last_service_mileage: int, tire_wear_values: List[float]) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear_values)
        return Car(engine, battery, tires)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int,
                      last_service_mileage: int, tire_wear_values: List[float]) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear_values)
        return Car(engine, battery, tires)
