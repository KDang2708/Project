# from datetime import date
# from domain.models.Giang_Vien.Giang_Vien import GiangVien
# from domain.models.Sinh_Vien.Sinh_Vien import SinhVien as HocSinh
# class NhiemVu:
#     def __init__(self, id_nguoi_thuc_hien: HocSinh, ngay_bat_dau: date, ngay_ket_thuc: date, id_nguoi_tao: GiangVien | HocSinh):
#         self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.id_nguoi_thuc_hien = id_nguoi_thuc_hien
#         self.ngay_bat_dau = ngay_bat_dau
#         self.ngay_ket_thuc = ngay_ket_thuc
#         self.id_nguoi_tao = id_nguoi_tao
from infrastructure.databases.base import Base
from sqlalchemy import Column, String, Date
class NhiemVuORM(Base):
    __tablename__ = "nhiem_vu"  # tên bảng trong cơ sở dữ liệu

    id = Column(String, primary_key=True)          # cột ID, kiểu String, là khóa chính
    id_nguoi_thuc_hien = Column(String)            # cột ID người thực hiện, kiểu String
    ngay_bat_dau = Column(Date)                    # cột ngày bắt đầu, kiểu Date
    ngay_ket_thuc = Column(Date)                   # cột ngày kết thúc, kiểu Date
    id_nguoi_tao = Column(String)                  # cột ID người tạo, kiểu String
    