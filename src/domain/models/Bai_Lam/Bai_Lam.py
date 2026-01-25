#Bài Làm(IDBaiKiemTra(String), NoiDungBaiLam(String), IDSinhVienThucHien(String))
from domain.models.Bai_Kiem_Tra.Bai_Kiem_Tra import BaiKiemTra
from domain.models.Nhiem_Vu.Nhiem_Vu import NhiemVu
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien as HocSinh
class BaiLam:
    def __init__(self, noi_dung_bai_lam: str, loai_bai_lam: int,bai_kiem_tra : BaiKiemTra|NhiemVu, sinh_vien_thuc_hien: HocSinh):
        self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
        self.noi_dung_bai_lam = noi_dung_bai_lam
        self.loai_bai_lam = loai_bai_lam
        self.bai_kiem_tra = bai_kiem_tra
        self.sinh_vien_thuc_hien = sinh_vien_thuc_hien