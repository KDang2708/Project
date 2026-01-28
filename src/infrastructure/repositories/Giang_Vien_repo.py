from domain.models.Giang_Vien.Giang_Vien import GiangVien
from domain.models.Giang_Vien.iGiang_Vien import IGiangVienRepository
from infrastructure.models.Giang_Vien_Model import GiangVienORM
from sqlalchemy.orm import Session
from domain.models.Tai_Khoan.iTai_Khoan import ITaiKhoanRepository

class GiangVienRepository(IGiangVienRepository):
    def __init__(self , sesion : Session , tai_khoan : ITaiKhoanRepository ):
        self.session = sesion
        self.repo_tai_khoan = tai_khoan
    def get_by_id(self, id_giang_vien : str)->GiangVien:
        orm = self.session.query(GiangVienORM).filter(GiangVienORM.id == id_giang_vien).first()
        tai_khoan = self.repo_tai_khoan.get_by_id(orm.id_tai_khoan)
        return GiangVien(
            id=orm.id,
            ten=orm.ten,
            tai_khoan=tai_khoan
        )