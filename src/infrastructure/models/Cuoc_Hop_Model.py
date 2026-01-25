# class CuocHop:
#     def __init__(self, thoi_gian_bat_dau: datetime, nguoi_tao: GiangVien|HocSinh, lop_hoc: LopHoc , nhom: Nhom | None = None):
#         self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.thoi_gian_bat_dau = thoi_gian_bat_dau
#         self.nguoi_tao = nguoi_tao
#         self.lop_hoc = lop_hoc
#         self.nhom = nhom
from infrastructure.databases.base import Base
from sqlalchemy import Column, String, DateTime
class CuocHopORM(Base):
    __tablename__ = "cuoc_hop"  # tên bảng trong cơ sở dữ liệu

    id = Column(String, primary_key=True)          # cột ID, kiểu String, là khóa chính
    thoi_gian_bat_dau = Column(DateTime)           # cột thời gian bắt đầu, kiểu DateTime
    id_nguoi_tao = Column(String)                   # cột ID người tạo, kiểu String
    id_lop_hoc = Column(String)                     # cột ID lớp học, kiểu String
    id_nhom = Column(String, nullable=True)                        # cột ID nhóm, kiểu String
