from domain.models.Moc_Quan_Trong.Moc_Quan_Trong import MocQuanTrong
from domain.models.Moc_Quan_Trong.iMoc_Quan_trong import IMocQuanTrongRepository
from infrastructure.models.Moc_Quan_trong_Model import MocQuanTrongORM
from domain.models.Mon_Hoc.Mon_Hoc import MonHoc
from sqlalchemy.orm import Session

class MocQuanTrongRepository(IMocQuanTrongRepository):
    def __init__(self , session : Session ):
        self.session = session
    def get_by_mon_hoc(self, mon_hoc : MonHoc)->list[MocQuanTrong]:
        orm = self.session.query(MocQuanTrongORM).filter(MocQuanTrongORM.id_mon_hoc == mon_hoc.id).all()
        return [ MocQuanTrong(
            noi_dung= o.noi_dung,
            mon_hoc=mon_hoc,
            id=o.id,
            loai_moc=o.loai_moc
        )
        for o in orm 
        ]
    