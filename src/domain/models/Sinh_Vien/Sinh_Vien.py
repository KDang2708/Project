from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan
class SinhVien:
    def __init__(self, ten: str, tai_khoan: TaiKhoan | None = None):
        self.id = None # ID sẽ được gán khi lưu vào cơ sở dữ liệu
        self.ten = ten
        self.tai_khoan = tai_khoan