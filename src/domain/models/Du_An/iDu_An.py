from abc import ABC, abstractmethod
from domain.models.Du_An.Du_An import DuAn

class IDuAn(ABC):
    @abstractmethod
    def add(self, du_an: DuAn) -> DuAn:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> DuAn | None:
        pass