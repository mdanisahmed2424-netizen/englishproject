# 🎯 Quick Deploy - 3 Simple Steps

## ✅ Your Setup
- Models: `anis80/anisproject` on HuggingFace ✅
- Backend: Ready to deploy (downloads models automatically)
- Frontend: Ready for Vercel

---

## 🚀 Deploy in 3 Steps

### Step 1: Push to GitHub (2 min)
```powershell
cd e:\anis
git remote add origin https://github.com/YOUR_USERNAME/sentiment-backend.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy Backend (3 min)

**Option A - Render (Recommended):**
1. https://render.com → Sign up with GitHub
2. New Web Service → Select your repo
3. Start: `uvicorn app:app --host 0.0.0.0 --port $PORT`
4. Plan: Free → Deploy

**Option B - HuggingFace:**
```powershell
git remote add hf https://huggingface.co/spaces/anis80/sentiment-api
git push hf main
```

### Step 3: Deploy Frontend (2 min)
1. Update `index.html` lines 72-73 with your backend URL
2. Push to GitHub
3. https://vercel.com → Import repo → Deploy

---

## ✅ Test
- Backend: `https://YOUR_URL/docs`
- Frontend: Enter text → Click Analyze → See result!

---

**Total Time: ~7 minutes | Cost: $0/month** 🎉

See `final_deployment.md` for detailed instructions.
