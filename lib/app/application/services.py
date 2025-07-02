import os
import shutil
from lib.app.domain.dtos import UploadRequestDTO, UploadResponseDTO
from lib.app.application.helpers import parse_xlsx
from lib.app.adapter.output.persistence.mongo_repository import MongoRepository
from lib.app.adapter.output.persistence.s3_adapter import S3Adapter
from core.config import config

class FileService:
    def __init__(self):
        self.upload_dir = config.get("UPLOAD_DIR", "uploads")
        os.makedirs(self.upload_dir, exist_ok=True)
        self.mongo_repo = MongoRepository()
        self.s3_adapter = S3Adapter()

    async def process_file_upload(self, request: UploadRequestDTO) -> UploadResponseDTO:
        try:
            file = request.file
            local_path = os.path.join(self.upload_dir, file.filename)
            with open(local_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            parts = parse_xlsx(local_path)
            await self.s3_adapter.upload_file(local_path, file.filename)
            await self.mongo_repo.insert_many(parts)

            return UploadResponseDTO(success=True, message="File processed successfully")
        except Exception as e:
            return UploadResponseDTO(success=False, message=str(e))