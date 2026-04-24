from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel

# Load model
with open("health_model.pkl", "rb") as f:
    model, scaler = pickle.load(f)

app = FastAPI()

# Input schema
class Patient(BaseModel):
    age: float
    sex: float
    cp: float
    trestbps: float
    chol: float
    fbs: float
    restecg: float
    thalach: float
    exang: float
    oldpeak: float
    slope: float
    ca: float
    thal: float

@app.get("/")
def home():
    return {"message": "Healthcare Prediction API Running"}

@app.post("/predict")
def predict(data: Patient):
    input_data = np.array([[
        data.age, data.sex, data.cp, data.trestbps,
        data.chol, data.fbs, data.restecg, data.thalach,
        data.exang, data.oldpeak, data.slope, data.ca, data.thal
    ]])

    prediction = model.predict(input_data)[0]

    return {"prediction": int(prediction)}