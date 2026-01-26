from domain.models.Du_An.Du_An import DuAn
from domain.models.Du_An.iDu_An import IDuAn
from infrastructure.models.Du_An_Model import DuAnORM
from sqlalchemy.orm import Session
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc

class DuAnRepository(IDuAn):
    def __init__(self, session : Session):
        self.session = session
    def add(self, du_an : DuAn)-> DuAn:
        orm = DuAnORM(
            noi_dung = du_an.noi_dung,
            id_nguoi_tao = du_an.nguoi_tao
        )
        self.session.add(orm)
        du_an.id = orm.id
        du_an.trang_thai = orm.trang_thai
        return du_an
    def set_lop(self, du_an : DuAn, lop_hoc : LopHoc)->DuAn:
        orm = self.session.query(DuAnORM).filter(DuAnORM.id == du_an.id).first()
        if orm is None:
            raise Exception("Dự án không tồn tại")
        orm.id_lop_hoc = lop_hoc.id
        du_an.lop_hoc = lop_hoc
        self.commit()
        return du_an