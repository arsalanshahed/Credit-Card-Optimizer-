# 🚀 Quick Deploy Guide

## Prerequisites
- GitHub account
- Render account (free tier)
- Vercel account (free tier)

## Step 1: Push to GitHub

```bash
cd credit-card-optimizer
git init
git add .
git commit -m "Initial MVP commit"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

## Step 2: Deploy Backend to Render

1. Go to https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure:
   - **Name**: `cc-optimizer-backend`
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Click **"Create Web Service"**
6. Wait for deployment (2-3 minutes)
7. **Copy the service URL** (e.g., `https://cc-optimizer-backend.onrender.com`)

## Step 3: Deploy Frontend to Vercel

1. Go to https://vercel.com/dashboard
2. Click **"Add New..."** → **"Project"**
3. Import your GitHub repository
4. Configure:
   - **Framework Preset**: Next.js
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`
5. **Environment Variables**:
   - `NEXT_PUBLIC_API_URL`: `https://your-backend-url.onrender.com`
6. Click **"Deploy"**
7. Wait for deployment (1-2 minutes)

## Step 4: Update CORS (if needed)

If you get CORS errors, update `backend/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend.vercel.app", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## ✅ Done!

Your app is live:
- Frontend: `https://your-app.vercel.app`
- Backend: `https://your-backend.onrender.com`
- API Docs: `https://your-backend.onrender.com/docs`

## 🧪 Test Deployment

```bash
curl https://your-backend.onrender.com/api/optimizer/cards
```

