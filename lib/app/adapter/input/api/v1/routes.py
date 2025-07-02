from fastapi import APIRouter, UploadFile, File
from lib.app.application.container import Container
from lib.app.domain.dtos import UploadRequestDTO

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    service = Container.get_file_service()
    request_dto = UploadRequestDTO(file=file)
    response = await service.process_file_upload(request_dto)
    return response