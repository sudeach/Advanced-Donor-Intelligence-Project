from fastapi import FastAPI

app = FastAPI(title="Donor Intelligence API")

@app.get("/")
def home():
    return {"message": "Donor Intelligence Platform Running"}

@app.post("/predict_churn")
def predict_churn(data: dict):
    return {
        "donor_id": data.get("donor_id"),
        "churn_probability": 0.15
    }