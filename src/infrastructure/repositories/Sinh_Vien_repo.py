from domain.models.Sinh_Vien.Sinh_Vien import SinhVien
from domain.models.Sinh_Vien.iSinh_Vien import ISinhVienRepository
from infrastructure.models.Sinh_Vien_Model import SinhVienORM
from sqlalchemy.orm import Session
from domain.models.Tai_Khoan.iTai_Khoan import ITaiKhoanRepository
class SinhVienRepository(ISinhVienRepository):
    def __init__(self,session : Session , tai_khoan : ITaiKhoanRepository ):
        self.session = session
        self.repo_tai_khoan = tai_khoan
    def get_by_id(self, id_sinh_vien : str)->SinhVien:
        orm = self.session.query(SinhVienORM).filter(SinhVienORM.id==id_sinh_vien).first()
        tai_khoan = self.repo_tai_khoan.get_by_id(orm.id_tai_khoan)
        return SinhVien(
            id=orm.id,
            ten=orm.ten,
            tai_khoan=tai_khoan
        )
    