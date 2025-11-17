# 🚀 Quick Deployment Guide

## Prerequisites
- GitHub account with repository: `https://github.com/arsalanshahed/Credit-Card-Optimizer-.git`
- Render account (free tier): https://dashboard.render.com
- Vercel account (free tier): https://vercel.com

---

## Step 1: Deploy Backend to Render (5 minutes)

### Option A: Using Render Dashboard (Recommended)

1. **Go to Render Dashboard**
   - Visit: https://dashboard.render.com
   - Sign in with GitHub

2. **Create New Web Service**
   - Click **"New +"** → **"Web Service"**
   - Select your repository: `Credit-Card-Optimizer-`
   - Click **"Connect"**

3. **Configure Service**
   - **Name**: `credit-card-optimizer-backend`
   - **Environment**: `Python 3`
   - **Region**: Choose closest to you
   - **Branch**: `main`
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Instance Type**: `Free`

4. **Environment Variables**
   - Click **"Advanced"** → **"Add Environment Variable"**
   - Add: `PYTHON_VERSION` = `3.11.6`

5. **Deploy**
   - Click **"Create Web Service"**
   - Wait 3-5 minutes for deployment
   - **Copy the service URL** (e.g., `https://credit-card-optimizer-backend.onrender.com`)

### Option B: Using render.yaml (Automatic)

1. **Push render.yaml to GitHub** (already done)
2. **Go to Render Dashboard** → **"New +"** → **"Blueprint"**
3. **Select your repository**
4. Render will auto-detect `render.yaml` and create the service
5. **Copy the service URL**

---

## Step 2: Deploy Frontend to Vercel (5 minutes)

### Option A: Using Vercel Dashboard (Recommended)

1. **Go to Vercel Dashboard**
   - Visit: https://vercel.com/dashboard
   - Sign in with GitHub

2. **Import Project**
   - Click **"Add New..."** → **"Project"**
   - Select repository: `Credit-Card-Optimizer-`
   - Click **"Import"**

3. **Configure Project**
   - **Framework Preset**: `Next.js` (auto-detected)
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build` (auto-detected)
   - **Output Directory**: `.next` (auto-detected)
   - **Install Command**: `npm install` (auto-detected)

4. **Environment Variables**
   - Click **"Environment Variables"**
   - Add: `NEXT_PUBLIC_API_URL` = `https://your-backend-url.onrender.com`
     - Replace `your-backend-url` with your actual Render backend URL from Step 1

5. **Deploy**
   - Click **"Deploy"**
   - Wait 2-3 minutes for deployment
   - **Copy the frontend URL** (e.g., `https://credit-card-optimizer.vercel.app`)

### Option B: Using Vercel CLI

```bash
cd frontend
npm install -g vercel
vercel login
vercel --prod
# When prompted, set NEXT_PUBLIC_API_URL environment variable
```

---

## Step 3: Update CORS (If Needed)

If you get CORS errors:

1. **Go to Render Dashboard** → Your backend service
2. **Go to "Environment"** tab
3. **Add Environment Variable**:
   - Key: `ENVIRONMENT`
   - Value: `production`
4. **Redeploy** the service

Or manually update `backend/main.py` to include your Vercel URL in `allow_origins`.

---

## Step 4: Test Deployment

1. **Test Backend**:
   - Visit: `https://your-backend.onrender.com/docs`
   - Should see FastAPI Swagger UI
   - Test endpoint: `POST /api/optimizer/recommend`

2. **Test Frontend**:
   - Visit: `https://your-app.vercel.app`
   - Navigate to `/optimizer`
   - Enter spending amounts
   - Click "Find Best Cards"
   - Should see recommendations

---

## 🎉 You're Live!

- **Frontend**: `https://your-app.vercel.app`
- **Backend**: `https://your-backend.onrender.com`
- **API Docs**: `https://your-backend.onrender.com/docs`

---

## 🔧 Troubleshooting

### Backend Issues

**Problem**: Build fails
- Check Render logs
- Verify `requirements.txt` is in `backend/` directory
- Ensure Python 3.11.6 is selected

**Problem**: 500 errors
- Check Render logs
- Verify `credit_cards.csv` is in `backend/data/`
- Check that all services are imported correctly

**Problem**: CORS errors
- Update `allow_origins` in `backend/main.py` with your Vercel URL
- Or set `ENVIRONMENT=production` in Render

### Frontend Issues

**Problem**: API calls fail
- Verify `NEXT_PUBLIC_API_URL` is set correctly in Vercel
- Check browser console for errors
- Ensure backend is running

**Problem**: Build fails
- Check Vercel build logs
- Verify Node.js 18+ is being used
- Check that all dependencies are in `package.json`

---

## 📝 Quick Reference

### Backend URLs
- Render Dashboard: https://dashboard.render.com
- Your Backend: `https://credit-card-optimizer-backend.onrender.com` (replace with your actual URL)

### Frontend URLs
- Vercel Dashboard: https://vercel.com/dashboard
- Your Frontend: `https://credit-card-optimizer.vercel.app` (replace with your actual URL)

### Environment Variables

**Render (Backend)**:
- `PYTHON_VERSION`: `3.11.6`

**Vercel (Frontend)**:
- `NEXT_PUBLIC_API_URL`: `https://your-backend.onrender.com`

---

**Need help?** Check the full [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed instructions.
