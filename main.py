from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from typing import List

app = FastAPI()

# Configuración de la conexión a MongoDB
client = MongoClient("mongodb://mongo:27017/")
db = client.sensordata
collection = db.data

class SensorData(BaseModel):
    sensor_id: str
    temperature: float
    humidity: float

@app.post("/sensor-data/")
async def create_sensor_data(data: SensorData):
    try:
	#Insertar los datos en MongoDB
	result = collection.insert_one(data.dict())
    	return {"status": "success", "id": str(result.inserted_id)}
    except Exception as e:
	raise HTTPException(status_code=500, detail="Error inserting data")

@app.get("/sensor-data/", response_model=List[SensorData])
async def get_all_sensor_data():
    sensor_data = list(collection.find({}))
    return sensor_data

@app.get("/sensor-data/{sensor_id}", response_model=SensorData)
async def get_sensor_data(sensor_id: str):
    sensor_data = collection.find_one({"sensor_id": sensor_id})
    if sensor_data:
        return sensor_data
    raise HTTPException(status_code=404, detail="Sensor data not found")

@app.delete("/sensor-data/{sensor_id}")
async def delete_sensor_data(sensor_id: str):
    result = collection.delete_one({"sensor_id": sensor_id})
    if result.deleted_count == 1:
        return {"status": "success"}
    raise HTTPException(status_code=404, detail="Sensor data not found")

@app.get("/")
async def read_root():
    return {"message": "FastAPI + MongoDB IoT Data Service"}
