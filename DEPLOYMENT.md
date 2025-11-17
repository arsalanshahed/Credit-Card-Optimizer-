# Deployment Guide

## 🚀 Deploy Backend to Render

### Step 1: Prepare Backend

1. **Create a GitHub repository** and push your code:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-repo-url>
git push -u origin main
```

2. **Ensure `render.yaml` is in the root** (already created)

### Step 2: Deploy on Render

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure:
   - **Name**: `cc-optimizer-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Root Directory**: `backend`

5. **Environment Variables** (if needed):
   - `PYTHON_VERSION`: `3.11.0`

6. Click **"Create Web Service"**

7. **Copy the service URL** (e.g., `https://cc-optimizer-backend.onrender.com`)

### Step 3: Update Frontend Environment

Update `frontend/.env.production`:
```
NEXT_PUBLIC_API_URL=https://your-backend-url.onrender.com
```

---

## 🌐 Deploy Frontend to Vercel

### Step 1: Prepare Frontend

1. **Update API URL** in `frontend/.env.production`:
```
NEXT_PUBLIC_API_URL=https://your-backend-url.onrender.com
```

2. **Ensure `vercel.json` is configured** (already created)

### Step 2: Deploy on Vercel

#### Option A: Vercel CLI

```bash
cd frontend
npm install -g vercel
vercel login
vercel --prod
```

#### Option B: Vercel Dashboard

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
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

---

## 🔧 Environment Variables

### Backend (Render)

- `PYTHON_VERSION`: `3.11.0`
- `PORT`: Auto-set by Render

### Frontend (Vercel)

- `NEXT_PUBLIC_API_URL`: Your Render backend URL

---

## ✅ Post-Deployment Checklist

1. ✅ Backend is accessible at Render URL
2. ✅ Frontend is accessible at Vercel URL
3. ✅ API calls from frontend work (check browser console)
4. ✅ CORS is configured correctly
5. ✅ Environment variables are set

---

## 🐛 Troubleshooting

### Backend Issues

**Problem**: 500 errors
- Check Render logs
- Verify CSV file is in `backend/data/`
- Ensure models directory exists

**Problem**: CORS errors
- Update `allow_origins` in `backend/main.py` with Vercel URL

### Frontend Issues

**Problem**: API calls fail
- Verify `NEXT_PUBLIC_API_URL` is set correctly
- Check browser network tab for actual request URL
- Ensure backend is running

**Problem**: Build fails
- Check Node.js version (18+)
- Verify all dependencies in `package.json`

---

## 📝 Quick Deploy Commands

```bash
# Backend (Render)
# - Use Render dashboard or:
render deploy

# Frontend (Vercel)
cd frontend
vercel --prod
```

---

**Your app will be live at:**
- Frontend: `https://your-app.vercel.app`
- Backend: `https://your-backend.onrender.com`


