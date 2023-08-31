from abc import ABC, abstractmethod
from typing import List


class Tires(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        pass
