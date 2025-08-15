from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
import pickle
import os
import uvicorn

# Initialize FastAPI
app = FastAPI(title="Medical Insurance Premium Predictor API")

# Define input schema
class InsuranceInput(BaseModel):
    age: int
    sex: str  # "male" or "female"
    bmi: float
    children: int
    smoker: str  # "yes" or "no"
    region: str  # "northwest", "northeast", "southeast", "southwest"

# Encoding dictionaries
sex_map = {"male": 0, "female": 1}
smoker_map = {"yes": 1, "no": 0}
region_map = {"northwest": 0, "northeast": 1, "southeast": 2, "southwest": 3}

# Load the saved model
try:
    with open("Insurance_ML.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    model = None
    print(f"Model loading failed: {e}")

# Health check endpoint
@app.get("/")
def read_root():
    return {"message": "Medical Insurance Premium Predictor API is running."}

# Prediction endpoint
@app.post("/predict")
def predict_premium(data: InsuranceInput):
    if model is None:
        return {"error": "Model not loaded. Check server logs."}
    try:
        input_df = pd.DataFrame([{
            "age": data.age,
            "sex": data.sex.lower(),
            "bmi": data.bmi,
            "children": data.children,
            "smoker": data.smoker.lower(),
            "region": data.region.lower()
        }])

        # Encode categorical variables
        input_df["sex"] = input_df["sex"].map(sex_map)
        input_df["smoker"] = input_df["smoker"].map(smoker_map)
        input_df["region"] = input_df["region"].map(region_map)

        prediction = model.predict(input_df)[0]
        return {"predicted_premium": round(float(prediction), 2)}
    
    except Exception as e:
        return {"error": str(e)}

# Run locally / on Railway
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port)

API = "https://f-api-production.up.railway.app/docs"