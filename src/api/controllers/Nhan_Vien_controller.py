from fastapi import HTTPException , status

from services.Tao_Mon_Hoc import TaoMonHocUseCase
from api.schemas.requests.Tao_Mon_Hoc import TaoMonHocRequest
from api.schemas.responses.Mon_Hoc import MonHocResponse
from services.Xem_Mon_Hoc import XemMonHocUseCase
from domain.models.Mon_Hoc.Mon_Hoc import MonHoc
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from api.schemas.requests.Tao_Lop_hoc import TaoLopHocRequest
from api.schemas.responses.Tao_Lop_Hoc import TaoLopHocResponse
from services.Tao_Lop_Hoc import TaoLopHocUseCase

class NhanVienController:
    def __init__(self , tao_mon_hoc : TaoMonHocUseCase , xem_mon_hoc : XemMonHocUseCase , tao_lop_hoc : TaoLopHocUseCase):
        self.ser_tao_mon_hoc = tao_mon_hoc
        self.ser_xem_mon_hoc = xem_mon_hoc
        self.ser_tao_lop_hoc = tao_lop_hoc
    def tao_mon_hoc(self , request : TaoMonHocRequest)->MonHocResponse:
        try: 
            mon_hoc=self.ser_tao_mon_hoc.execute(request.ten_mon_hoc , request.tin_chi , request.de_cuong)
            return MonHocResponse(
                id_mon_hoc=mon_hoc.id,
                ten_mon_hoc=mon_hoc.ten,
                tin_chi=mon_hoc.tin_chi,
                de_cuong=mon_hoc.de_cuong
            )
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_405_METHOD_NOT_ALLOWED, 
                detail=str(e)
            )
    def xem_mon_hoc(self)->list[MonHocResponse]:
        try:
            dsMH : list[MonHoc] = self.ser_xem_mon_hoc.execute()
            return [
                MonHocResponse(
                    id_mon_hoc=MH.id,
                    ten_mon_hoc=MH.ten,
                    tin_chi=MH.tin_chi,
                    de_cuong=MH.de_cuong
                )
                for MH in dsMH
            ]
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
            )
    def tao_lop_hoc(self , request : TaoLopHocRequest)->TaoLopHocResponse:
        try:
            lop_hoc : LopHoc = self.ser_tao_lop_hoc.execute(request.id_mon_hoc , request.id_giang_vien)
            return TaoLopHocResponse(
                id_lop_hoc=lop_hoc.id,
                id_mon_hoc=lop_hoc.mon_hoc.id,
                ten_mon_hoc=lop_hoc.mon_hoc.ten,
                tin_chi=lop_hoc.mon_hoc.tin_chi,
                id_giang_vien=lop_hoc.giang_vien.id
            )
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
            )