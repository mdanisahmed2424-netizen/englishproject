from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import os
from pathlib import Path
from huggingface_hub import hf_hub_download

# Initialize FastAPI app
app = FastAPI(
    title="Sentiment Analysis API",
    description="API for sentiment analysis using ensemble ML models",
    version="1.0.0"
)

# Configure CORS - allow all origins for Vercel frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your Vercel domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request/response models
class TextInput(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    predicted_sentiment: str
    input_text: str

class StatusResponse(BaseModel):
    status: str
    model_name: str
    message: str

# Global variables for models
label_encoder = None
tfidf_vectorizer = None
voting_classifier = None
MODEL_NAME = "Voting Classifier (KNN + RF + ET)"

# HuggingFace Model Hub configuration
REPO_ID = "anis80/anisproject"  # Your HuggingFace model repository
MODEL_FILES = {
    "label_encoder": "label_encoder.joblib",
    "tfidf_vectorizer": "tfidf_vectorizer.joblib",
    "voting_classifier": "voting_classifier_knn_rf_et-001.joblib"
}

def download_model_from_hub(filename: str) -> str:
    """Download a model file from HuggingFace Model Hub"""
    try:
        print(f"📥 Downloading {filename} from HuggingFace Model Hub...")
        file_path = hf_hub_download(
            repo_id=REPO_ID,
            filename=filename,
            cache_dir="./model_cache"
        )
        print(f"✅ Downloaded {filename}")
        return file_path
    except Exception as e:
        print(f"❌ Error downloading {filename}: {str(e)}")
        raise e

# Load models on startup
@app.on_event("startup")
async def load_models():
    global label_encoder, tfidf_vectorizer, voting_classifier
    
    try:
        print(f"🚀 Starting model loading from HuggingFace: {REPO_ID}")
        
        # Download and load each model
        label_encoder_path = download_model_from_hub(MODEL_FILES["label_encoder"])
        label_encoder = joblib.load(label_encoder_path)
        
        tfidf_path = download_model_from_hub(MODEL_FILES["tfidf_vectorizer"])
        tfidf_vectorizer = joblib.load(tfidf_path)
        
        classifier_path = download_model_from_hub(MODEL_FILES["voting_classifier"])
        voting_classifier = joblib.load(classifier_path)
        
        print("✅ All models loaded successfully from HuggingFace Model Hub!")
        
    except Exception as e:
        print(f"❌ Error loading models: {str(e)}")
        print(f"⚠️  Make sure models are uploaded to: https://huggingface.co/{REPO_ID}")
        raise e

# Health check endpoint
@app.get("/")
async def root():
    return {
        "message": "Sentiment Analysis API is running",
        "model_source": f"HuggingFace: {REPO_ID}",
        "endpoints": {
            "predict": "/predict",
            "status": "/status",
            "docs": "/docs"
        }
    }

# Status endpoint
@app.get("/status", response_model=StatusResponse)
async def get_status():
    if voting_classifier is None:
        raise HTTPException(status_code=503, detail="Models not loaded")
    
    return StatusResponse(
        status="ready",
        model_name=MODEL_NAME,
        message=f"All models loaded from {REPO_ID}"
    )

# Prediction endpoint
@app.post("/predict", response_model=PredictionResponse)
async def predict_sentiment(input_data: TextInput):
    try:
        # Validate models are loaded
        if None in [label_encoder, tfidf_vectorizer, voting_classifier]:
            raise HTTPException(
                status_code=503, 
                detail="Models not loaded. Please try again later."
            )
        
        # Validate input
        if not input_data.text or not input_data.text.strip():
            raise HTTPException(
                status_code=400, 
                detail="Text input cannot be empty"
            )
        
        # Preprocess and transform the text
        text_tfidf = tfidf_vectorizer.transform([input_data.text])
        
        # Make prediction
        prediction = voting_classifier.predict(text_tfidf)
        
        # Decode the prediction
        sentiment = label_encoder.inverse_transform(prediction)[0]
        
        return PredictionResponse(
            predicted_sentiment=sentiment,
            input_text=input_data.text
        )
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Prediction error: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Prediction failed: {str(e)}"
        )

# For local testing
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
