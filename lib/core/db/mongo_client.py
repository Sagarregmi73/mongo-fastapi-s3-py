from motor.motor_asyncio import AsyncIOMotorClient
from lib.core.config import config

client = AsyncIOMotorClient(config.get("MONGO_URI"))
db = client[config.get("MONGO_DB")]
