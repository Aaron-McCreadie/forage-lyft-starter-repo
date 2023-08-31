from datetime import date

from ..interfaces import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        date_delta = self.current_date.day - self.last_service_date.day
        return date_delta > (365 * 2)
