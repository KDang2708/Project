from fastapi import HTTPException , status

from services.Xem_Lop_Hoc import XemLopHocUseCase
from api.schemas.responses.Xem_Lop_hoc import XemLopHocResponse
from services.Phan_Nhom import PhanNhomUseCase
from api.schemas.requests.Tao_Nhom import TaoNhomRequest
from api.schemas.responses.Tao_Nhom import TaoNhomResponse
from api.schemas.requests.Them_Sinh_Vien_Nhom import ThemSinhVienNhomRequest

class GiangVienController:
    def __init__(self , xem_lop_hoc : XemLopHocUseCase , phan_nhom : PhanNhomUseCase):
        self.ser_xem_lop_hoc = xem_lop_hoc
        self.ser_phan_nhom = phan_nhom

    def xem_lop_hoc(self)->list[XemLopHocResponse]:
        try:
            dsLH = self.ser_xem_lop_hoc.execute()
            return [
                XemLopHocResponse(
                    id_lop_hoc=LH.id,
                    id_mon_hoc=LH.mon_hoc.id,
                    ten_mon_hoc=LH.mon_hoc.ten,
                    id_giang_vien=LH.giang_vien.ten,
                )
                for LH in dsLH
            ]
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
            )
    def tao_nhom(self , request :TaoNhomRequest )->TaoNhomResponse:
        try:
            self.ser_phan_nhom.execute(request.id_lop_hoc)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
    def them_sinh_vien_vao_nhom(self, request : ThemSinhVienNhomRequest):
        try:
            self.ser_phan_nhom.them_sinh_vien(request.id_sinh_vien , request.id_nhom)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )