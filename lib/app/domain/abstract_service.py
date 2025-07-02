from abc import ABC, abstractmethod
from lib.app.domain.dtos import UploadRequestDTO, UploadResponseDTO

class AbstractFileService(ABC):
    @abstractmethod
    async def process_file_upload(self, request: UploadRequestDTO) -> UploadResponseDTO:
        pass