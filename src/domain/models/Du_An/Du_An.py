#Dự án(IDDuAn(String), NoiDungDuAn(String), TrangThai(Bool), IDNguoiTao(String))
from domain.models.Giang_Vien.Giang_Vien import GiangVien

class DuAn():
    def __init__(self, noi_dung: str, nguoi_tao: GiangVien):#hàm khởi tạo
        self.id = None
        self.noi_dung = noi_dung
        self.trang_thai = False
        self.nguoi_tao = nguoi_tao
