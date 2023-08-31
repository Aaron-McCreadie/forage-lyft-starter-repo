from datetime import date

from ..interfaces import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self._last_service_date = last_service_date
        self._current_date = current_date

    def needs_service(self) -> bool:
        timedelta =  self._current_date - self._last_service_date
        return timedelta > 2