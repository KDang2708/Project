from abc import ABC, abstractmethod
from domain.models.Bai_Kiem_Tra.Bai_Kiem_Tra import BaiKiemTra
class IBaiKiemTraRepository(ABC):
    @abstractmethod
    def add(self, bai_kiem_tra: BaiKiemTra) -> BaiKiemTra:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> BaiKiemTra | None:
        pass