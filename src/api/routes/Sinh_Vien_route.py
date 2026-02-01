from fastapi import APIRouter , Depends

from api.controllers.Sinh_Vien_controller import SinhVienController
from services.Xem_Lop_Hoc import XemLopHocUseCase
from api.schemas.responses.Xem_Lop_hoc import XemLopHocResponse
from infrastructure.security.dependency import get_current_user
from api.schemas.responses.Xem_Chi_Tiet_Lop_Hoc import XemChiTietLopHocResponse
from api.schemas.requests.Xem_Chi_Tiet_Lop_Hoc import XemChiTietLopHocRequest
from services.Xem_Nhom import XemNhomUseCase
from api.schemas.responses.Xem_Nhom_SV import XemNhomSVResponse
from api.schemas.requests.Xem_Nhom_SV import XemNhomSVRequest
from services.Xem_Thong_Tin_Lop_Hoc import XemThongTinLopHocUseCase
from api.schemas.responses.Xem_Thong_Tin_Lop_Hoc import XemThongTinLopHocResponse
from api.schemas.requests.Xem_Thong_Tin_Lop_Hoc import XemThongTinLopHocRequest

router = APIRouter(prefix="/sinh_vien" , tags=["SinhVien"])

def get_sinh_vien_controller():
    return SinhVienController(
        xem_lop_hoc=XemLopHocUseCase(),
        xem_nhom=XemNhomUseCase(),
        xem_thong_tin_lop_hoc=XemThongTinLopHocUseCase(),
    )

@router.get("/xem_lop_hoc",response_model=list[XemLopHocResponse],status_code=200)
def xem_lop_hoc(
    user = Depends(get_current_user),
    controller : SinhVienController = Depends(get_sinh_vien_controller)
):
    return controller.xem_lop_hoc()
@router.get("/xem_chi_tiet_lop_hoc",response_model=XemChiTietLopHocResponse,status_code=200)
def xem_chi_tiet_lop_hoc(
    request : XemChiTietLopHocRequest,
    user = Depends(get_current_user),
    controller : SinhVienController = Depends(get_sinh_vien_controller)
):
    return controller.xem_chi_tiet_lop_hoc(request)
@router.get("/xem_nhom", response_model=XemNhomSVResponse , status_code=200)
def xem_nhom(
    request : XemNhomSVRequest,
    user = Depends(get_current_user),
    controller : SinhVienController = Depends(get_sinh_vien_controller)
):
    return controller.xem_nhom_sinh_vien(request)
@router.get("/xem_thong_tin_lop_hoc", response_model=XemThongTinLopHocResponse, status_code=200)
def xem_thong_tin_lop_hoc(
    request : XemThongTinLopHocRequest,
    user = Depends(get_current_user),
    controller : SinhVienController = Depends(get_sinh_vien_controller)
):
    return controller.ser_xem_thong_tin_lop_hoc(request)