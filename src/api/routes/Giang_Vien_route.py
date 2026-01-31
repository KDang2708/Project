from fastapi import APIRouter , Depends

from infrastructure.security.dependency import get_current_user
from api.controllers.Giang_Vien_controller import GiangVienController
from services.Xem_Lop_Hoc import XemLopHocUseCase
from api.schemas.responses.Xem_Lop_hoc import XemLopHocResponse
from api.schemas.responses.Tao_Nhom import TaoNhomResponse
from api.schemas.requests.Tao_Nhom import TaoNhomRequest
from services.Phan_Nhom import PhanNhomUseCase
from api.schemas.requests.Them_Sinh_Vien_Nhom import ThemSinhVienNhomRequest
from services.Xem_Nhom import XemNhomUseCase
from api.schemas.responses.Xem_Nhom import XemNhomResponse
from api.schemas.requests.Xem_Nhom import XemNhomRequest

router = APIRouter(prefix="/giang_vien",tags=["GiangVien"])

def get_giang_vien_controller():
    return GiangVienController(
        xem_lop_hoc = XemLopHocUseCase(),
        phan_nhom= PhanNhomUseCase(),
        xem_nhom= XemNhomUseCase(),
    )

@router.get("/xem_lop_hoc", response_model=list[XemLopHocResponse],status_code=200)
def xem_lop_hoc(
    user = Depends(get_current_user),
    controller : GiangVienController = Depends(get_giang_vien_controller)
):
    return controller.xem_lop_hoc()
@router.put("/tao_nhom",response_model=TaoNhomResponse , status_code=201)
def tao_nhom(
    request = TaoNhomRequest,
    user = Depends(get_current_user),
    controller : GiangVienController = Depends(get_giang_vien_controller)
):
    return controller.tao_nhom(request)
@router.put("/them_sinh_vien_nhom",status_code=200)
def them_sinh_vien_nhom(
    request : ThemSinhVienNhomRequest,
    user = Depends(get_current_user),
    controller : GiangVienController = Depends(get_giang_vien_controller)
):
    return controller.them_sinh_vien_vao_nhom(request)
@router.get("/xem_nhom",response_model=XemNhomResponse,status_code=200)
def xem_nhom(
    request : XemNhomRequest,
    user = Depends(get_current_user),
    controller : GiangVienController = Depends(get_giang_vien_controller)
):
    return controller.xem_nhom(request)