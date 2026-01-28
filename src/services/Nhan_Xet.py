from domain.models.Nhan_Xet.Nhan_Xet import NhanXet
from domain.models.Nhan_Xet.iNhan_Xet import INhanXetRepository

class NhanXetUseCase():
    def __init__(self, nhan_xet : INhanXetRepository ):
        self.repo_nhan_xet = nhan_xet
    def execute(self , )
        











# from infrastructure.databases.base import Base
# from sqlalchemy import Column , String , ForeignKey
# import uuid

# class NhiemVuORM(Base):
#     __tablename__ = "nhiem_vu"

#     id = Column(String , primary_key=True , default=lambda : str(uuid.uuid4()))
#     noi_dung_nhan_xet = Column(String)
#     id_giang_vien = Column(String , ForeignKey("giang_vien"))
#     id_bai_lam = Column(String, ForeignKey("bai_lam"))