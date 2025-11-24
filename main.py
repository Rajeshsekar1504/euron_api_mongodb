from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = AsyncIOMotorClient(MONGO_URL)
db = client["euron"]
euron_data = db["euron_coll"]

app = FastAPI()

class eurondata(BaseModel):
    name: str
    phone: int
    city: str
    course: str

@app.post("/euron/insert")
async def euron_data_insert_helper(data:eurondata):
    result = await euron_data.insert_one(data.dict())
    return str(result.inserted_id)

def euron_helper(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc

@app.get("/euron/getdata")
async def get_euron_data():
    items = []
    cursor = euron_data.find({})
    async for document in cursor:
        items.append(euron_helper(document))
    return items

@app.get("/euron/showdata")
async def show_euron_data():
    items = []
    cursor = euron_data.find({})
    async for document in cursor:
        items.append(euron_helper(document))
    return items