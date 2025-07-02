from core.db.mongo_client import db
from typing import List
from lib.app.domain.entities import PartData

class MongoRepository:
    def __init__(self):
        self.collection = db.parts

    async def insert_many(self, parts: List[PartData]):
        docs = [part.dict() for part in parts]
        await self.collection.insert_many(docs)
