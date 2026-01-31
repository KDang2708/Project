from fastapi import HTTPException , status

from services.Xem_Lop_Hoc import XemLopHocUseCase

class SinhVienController:
    def __init__(self , xem_lop_hoc : XemLopHocUseCase):
        self.ser_xem_lop_hoc = xem_lop_hoc
    def xem_lop_hoc()