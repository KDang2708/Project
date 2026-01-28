from domain.models.Bai_Kiem_Tra.Bai_Kiem_Tra import BaiKiemTra
from domain.models.Bai_Kiem_Tra.iBai_Kiem_Tra import IBaiKiemTraRepository
from infrastructure.models.Bai_Kiem_Tra_Model import BaiKiemTraORM
from sqlalchemy.orm import Session
from domain.models.Mon_Hoc.Mon_Hoc import MonHoc
from domain.models.Mon_Hoc.iMon_Hoc import IMonHocRepository

class BaiKiemTraRepository(IBaiKiemTraRepository):
    def __init__(self , session : Session , mon_hoc : IMonHocRepository):
        self.session = session
        self.repo_mon_hoc = mon_hoc
    def get_by_mon_hoc(self , mon_hoc : MonHoc )->list[BaiKiemTra]:
        orm_list = self.session.query(BaiKiemTraORM).filter(BaiKiemTraORM.id_mon_hoc==mon_hoc.id).all()
        return[
            BaiKiemTra(
                id= orm.id,
                tieu_de = orm.tieu_de,
                de_kiem_tra=orm.de_kiem_tra,
                mon_hoc= self.repo_mon_hoc.get_by_id(orm.id_mon_hoc)
            )
            for orm in orm_list
        ]
    
    def get_by_id(self, id_bai_kiem_tra : str)->BaiKiemTra:
        orm = self.session.query(BaiKiemTraORM).filter(BaiKiemTraORM.id==id_bai_kiem_tra).first()
        return BaiKiemTra(

        )