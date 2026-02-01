from fastapi import HTTPException , status

from services.Xem_Lop_Hoc import XemLopHocUseCase
from api.schemas.responses.Xem_Lop_hoc import XemLopHocResponse
from api.schemas.requests.Xem_Chi_Tiet_Lop_Hoc import XemChiTietLopHocRequest
from api.schemas.responses.Xem_Chi_Tiet_Lop_Hoc import XemChiTietLopHocResponse , SinhVienResponse
from api.schemas.requests.Xem_Nhom_SV import XemNhomSVRequest
from api.schemas.responses.Xem_Nhom_SV import XemNhomSVResponse , SinhVienResponse
from services.Xem_Nhom import XemNhomUseCase
from api.schemas.requests.Xem_Thong_Tin_Lop_Hoc import XemThongTinLopHocRequest
from api.schemas.responses.Xem_Thong_Tin_Lop_Hoc import XemThongTinLopHocResponse , LopHocResponse , MocQuanTrongResponse , BaiKiemTraResponse
from services.Xem_Thong_Tin_Lop_Hoc import XemThongTinLopHocUseCase

class SinhVienController:
    def __init__(self , xem_lop_hoc : XemLopHocUseCase, xem_nhom : XemNhomUseCase , xem_thong_tin_lop_hoc : XemThongTinLopHocUseCase):
        self.ser_xem_lop_hoc = xem_lop_hoc
        self.ser_xem_nhom = xem_nhom
        self.ser_xem_thong_tin_lop_hoc = xem_thong_tin_lop_hoc
    def xem_lop_hoc(self)->list[XemLopHocResponse]:
        try:
            dsLH = self.ser_xem_lop_hoc.execute()
            return [
                XemLopHocResponse(
                    id_lop_hoc=LH.id,
                    id_mon_hoc=LH.mon_hoc.id,
                    ten_mon_hoc=LH.mon_hoc.ten,
                    id_giang_vien=LH.giang_vien.id,
                    ten_giang_vien=LH.giang_vien.ten

                )
                for LH in dsLH
            ]
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
    def xem_chi_tiet_lop_hoc(self , request : XemChiTietLopHocRequest)->XemChiTietLopHocResponse:
        try:
            lop_hoc=self.ser_xem_lop_hoc.xem_chi_tiet(request.id_lop_hoc)
            return XemChiTietLopHocResponse(
                id_lop_hoc=lop_hoc.id,
                id_mon_hoc=lop_hoc.mon_hoc.id,
                ten_mon_hoc=lop_hoc.mon_hoc.ten,
                de_cuong=lop_hoc.mon_hoc.de_cuong,
                id_giang_vien=lop_hoc.giang_vien.id,
                ten_giang_vien=lop_hoc.giang_vien.ten,
                danh_sach_sinh_vien= [
                    SinhVienResponse(
                        SV.id,
                        SV.ten
                    )
                    for SV in lop_hoc.danh_sach_hoc_sinh
                ]
            )
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
    def xem_nhom_sinh_vien(self , request : XemNhomSVRequest)->XemNhomSVResponse:
        try:
            nhom = self.ser_xem_nhom.execute(request.id_nhom)
            return XemNhomSVResponse(
                id_nhom=nhom.id,
                danh_sach_sinh_vien= [
                    SinhVienResponse(
                        id_sinh_vien=SV.id,
                        ten_sinh_vien=SV.ten
                    )
                    for SV in nhom.danh_sach_hoc_sinh
                ]
            )
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
            )
    def xem_thong_tin_lop_hoc(self , request : XemThongTinLopHocRequest )->XemThongTinLopHocResponse:
        try:
            result = self.ser_xem_thong_tin_lop_hoc.execute(request.id_lop_hoc)

            return XemThongTinLopHocResponse(
                lop_hoc=LopHocResponse.from_orm(result["lop_hoc"]),

                ds_moc_quan_trong=[
                    MocQuanTrongResponse.from_orm(mq)
                    for mq in result["ds_moc_quan_trong"]
                ],

                ds_bai_kiem_tra=[
                    BaiKiemTraResponse.from_orm(bkt)
                    for bkt in result["ds_bai_kiem_tra"]
                ],
            )
        except HTTPException as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
            )