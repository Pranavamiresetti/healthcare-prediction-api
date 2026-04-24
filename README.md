# 🧠 Healthcare Prediction API

End-to-end Machine Learning system for predicting heart disease using patient data.

## 🚀 Live API Demo
Run locally:
http://127.0.0.1:8000/docs

## 🚀 Tech Stack
- Python
- Scikit-learn
- FastAPI
- Docker

## 📊 Model Performance
- Accuracy: ~81%
- Evaluated using precision, recall, F1-score

## ⚙️ Features
- REST API for real-time prediction
- Input validation using Pydantic
- Dockerized deployment

## 📌 API Endpoint
POST /predict

## 📥 Example Input
{
  "age": 52,
  "sex": 1,
  "cp": 0,
  "trestbps": 125,
  "chol": 212,
  "fbs": 0,
  "restecg": 1,
  "thalach": 168,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 2,
  "ca": 2,
  "thal": 3
}

## 📤 Output
{
  "prediction": 1
}

## 📦 Project Structure
healthcare-api/
│
├── main.py            # FastAPI app
├── health_model.pkl   # Trained ML model + scaler
├── Dockerfile         # Container setup
├── requirements.txt   # Dependencies

## 🧠 How it works
1. Input patient data via API
2. Data is scaled using StandardScaler
3. Model predicts heart disease (0/1)
4. API returns prediction

