from domain.models.Sinh_Vien.Sinh_Vien import SinhVien
from domain.models.Sinh_Vien.iSinh_Vien import ISinhVienRepository
from infrastructure.models.Sinh_Vien_Model import SinhVienORM
from sqlalchemy.orm import Session
class SinhVienRepository(ISinhVienRepository):
    def __init__(self,session : Session ):
        super().__init__()
    