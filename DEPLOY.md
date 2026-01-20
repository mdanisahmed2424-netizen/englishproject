# 🚀 Deployment Guide - Using HuggingFace Models

## ✅ Perfect Setup!

You've uploaded your models to HuggingFace at: **`anis80/anisproject`**

The app is now configured to download models from there automatically!

---

## 📤 Deploy to Render (Recommended - Free)

### Step 1: Push to GitHub

```powershell
cd e:\anis

# Add GitHub remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/sentiment-analysis-backend.git
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 2: Deploy to Render

1. Go to: **https://render.com**
2. Sign up with GitHub
3. Create **"New Web Service"**
4. Connect your `sentiment-analysis-backend` repository
5. Configure:
   - **Name**: `sentiment-analysis-api`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
   - **Instance Type**: **Free**
6. Click **"Create Web Service"**

### Step 3: Wait for Deployment (3-5 minutes)

Your API will be live at: `https://sentiment-analysis-api-XXXX.onrender.com`

---

## 🌐 Alternative: Deploy to HuggingFace Spaces

Since your models are already on HuggingFace, you can also deploy there:

### Create Space

1. Go to: https://huggingface.co/new-space
2. Name: `sentiment-analysis-api`
3. SDK: **Docker**
4. Hardware: **CPU basic (Free)**

### Push Code

```powershell
cd e:\anis

# Add HuggingFace remote
git remote add hf https://huggingface.co/spaces/anis80/sentiment-analysis-api
git push hf main
```

---

## ✅ Benefits of This Approach

- ✅ **No large files in repository** (only ~10KB of code)
- ✅ **Models downloaded on startup** from HuggingFace
- ✅ **Works on any platform** (Render, HuggingFace, Railway, etc.)
- ✅ **Easy model updates** - just update on HuggingFace
- ✅ **Free deployment** on both platforms

---

## 🧪 Test Locally First

```powershell
cd e:\anis
pip install -r requirements.txt
python app.py
```

Visit: http://localhost:7860/docs

---

## 📝 Update Frontend

Once deployed, update `index.html` lines 72-73:

```javascript
const predictApi = 'https://YOUR_DEPLOYMENT_URL/predict';
const statusApi = 'https://YOUR_DEPLOYMENT_URL/status';
```

Then deploy frontend to Vercel!

---

## 💰 Cost: $0/month 🎉

Both Render and HuggingFace offer free tiers perfect for this project!

---

**Ready to deploy?** Choose Render or HuggingFace and follow the steps above! 🚀
