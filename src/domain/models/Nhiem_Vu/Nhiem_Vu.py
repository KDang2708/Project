#Nhiệm vụ(IDNhiemVu(String), IDNguoiThucHien(String),
#NgayKetThuc(Date), NgayBatDau(Date), IDNguoiTao(String))
from datetime import date
from domain.models.Giang_Vien.Giang_Vien import GiangVien
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien as HocSinh
class NhiemVu:
    def __init__(self, id_nguoi_thuc_hien: HocSinh, ngay_bat_dau: date, ngay_ket_thuc: date, id_nguoi_tao: GiangVien | HocSinh):
        self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
        self.id_nguoi_thuc_hien = id_nguoi_thuc_hien
        self.ngay_bat_dau = ngay_bat_dau
        self.ngay_ket_thuc = ngay_ket_thuc
        self.id_nguoi_tao = id_nguoi_tao