from lib.app.application.services import FileService

class Container:
    _file_service = None

    @classmethod
    def get_file_service(cls) -> FileService:
        if cls._file_service is None:
            cls._file_service = FileService()
        return cls._file_service