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

# Full update
@app.put("/euron/update/{item_id}")
async def full_update_euron_data(item_id: str, data: eurondata):
    """
    Replaces the whole document with the new data.
    All fields are required.
    """
    result = await euron_data.replace_one(
        {"_id": ObjectId(item_id)},
        data.dict()
    )
    if result.matched_count == 0:
        return {"updated": False, "message": "Document not found"}
    return {"updated": True, "modified_count": result. modified_count}

# Partial update(PATCH)
@app.patch("/euron/update/{item_id}")
async def partial_update_euron_data(item_id: str, data: eurondata):
    """
    Updates only the fileds that are sent in the request body.
    """
    update_data = {k: v for k, v in data.dict().items() if v is not None}
    if not update_data:
        return {"updated": False, "message": "No fields to update"}

    result = await euron_data.update_one(
         {"_id": ObjectId(item_id)},
         {"$set": update_data}

    ) 

    if result.matched_count == 0:
        return {"updated": False, "message": "Document not found"}
    return {"updated": True, "modified_count": result.modified_count}


@app.delete("/euron/delete/{item_id}")
async def delete_euron_data(item_id : str):
    result = await euron_data.delete_one({"_id": ObjectId(item_id)})

    if result.deleted_count == 0:
        return {"deleted": False, "message": "Document not found"}
    
    return {"detailed": True}
    
