from pydantic import BaseModel
from fastapi import UploadFile

class UploadRequestDTO(BaseModel):
    file: UploadFile

class UploadResponseDTO(BaseModel):
    success: bool
    message: str