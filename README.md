# Sentiment Analysis API

A FastAPI-based sentiment analysis service using ensemble machine learning models (KNN, Random Forest, Extra Trees).

## Features

- **Fast predictions** using pre-trained ML models
- **RESTful API** with automatic documentation
- **CORS enabled** for web frontend integration
- **Ensemble learning** for improved accuracy

## API Endpoints

### `GET /`
Health check and API information

### `GET /status`
Returns model status and readiness

### `POST /predict`
Analyzes sentiment of input text

**Request body:**
```json
{
  "text": "Your text here"
}
```

**Response:**
```json
{
  "predicted_sentiment": "positive",
  "input_text": "Your text here"
}
```

## Models

This API uses three pre-trained models:
- **Label Encoder**: Encodes sentiment labels
- **TF-IDF Vectorizer**: Converts text to numerical features
- **Voting Classifier**: Ensemble of KNN, Random Forest, and Extra Trees

## Local Development

```bash
pip install -r requirements.txt
python app.py
```

The API will be available at `http://localhost:7860`

## Documentation

Interactive API documentation available at `/docs` (Swagger UI) and `/redoc` (ReDoc)
