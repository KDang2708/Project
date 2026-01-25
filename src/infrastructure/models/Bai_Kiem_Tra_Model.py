# from domain.models.Mon_Hoc.Mon_Hoc import MonHoc
# class BaiKiemTra:
#     def __init__(self, de_kiem_tra: list[str], mon_hoc: MonHoc):
#         self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.de_kiem_tra = de_kiem_tra
#         self.mon_hoc = mon_hoc
from infrastructure.databases.base import Base
from sqlalchemy import Column, String
class BaiKiemTraORM(Base):
    __tablename__ = "bai_kiem_tra"  # tên bảng trong cơ sở dữ liệu

    id = Column(String, primary_key=True)      # cột ID, kiểu String, là khóa chính
    de_kiem_tra = Column(String)                # cột đề kiểm tra, kiểu String
    id_mon_hoc = Column(String)                 # cột ID môn học liên kết, kiểu String