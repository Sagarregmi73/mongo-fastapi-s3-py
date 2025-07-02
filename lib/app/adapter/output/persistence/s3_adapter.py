import asyncio
from core.aws.s3_config import s3_client, bucket_name

class S3Adapter:
    async def upload_file(self, file_path: str, key: str):
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, lambda: s3_client.upload_file(file_path, bucket_name, key))