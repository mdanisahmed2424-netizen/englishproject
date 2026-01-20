---
title: Sentiment Analysis API
emoji: 😊
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# Sentiment Analysis API

A FastAPI-based sentiment analysis service using ensemble machine learning models (KNN, Random Forest, Extra Trees).

## Features

- **Fast predictions** using pre-trained ML models from HuggingFace Model Hub
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

This API downloads models from HuggingFace Model Hub: `anis80/anisproject`

- **Label Encoder**: Encodes sentiment labels
- **TF-IDF Vectorizer**: Converts text to numerical features  
- **Voting Classifier**: Ensemble of KNN, Random Forest, and Extra Trees

## Documentation

Interactive API documentation available at `/docs` (Swagger UI)
