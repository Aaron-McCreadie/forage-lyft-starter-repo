from datetime import date

from ..interfaces import Battery


class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
         self._last_service_date = last_service_date
         self._current_date = current_date

    def needs_service(self) -> bool:
        return self._current_date - self._last_service_date > 4
