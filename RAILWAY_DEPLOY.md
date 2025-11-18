# 🚂 Railway Deployment Guide

## Overview

This project is configured for **unified deployment** on Railway. Both the FastAPI backend and Next.js frontend run in a single container, eliminating CORS issues and simplifying deployment.

## 🚀 Quick Deploy (One-Click)

### Option 1: Deploy from GitHub

1. **Go to Railway**: https://railway.app
2. **Sign in** with GitHub
3. **Click "New Project"**
4. **Select "Deploy from GitHub repo"**
5. **Choose your repository**: `Credit-Card-Optimizer-`
6. **Railway will auto-detect**:
   - Dockerfile
   - Build settings
   - Start command
7. **Click "Deploy"** - That's it! 🎉

### Option 2: Deploy with Railway CLI

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Deploy
railway up
```

## ⚙️ Configuration

### Environment Variables

**No environment variables required!** Everything runs on the same domain.

Optional variables (if needed):
- `PORT` - Automatically set by Railway
- `ENVIRONMENT` - Set to `production` (optional)

### Build Process

1. **Stage 1**: Builds Next.js frontend (Node.js 18)
2. **Stage 2**: Sets up Python runtime
3. **Copies**: Built frontend to `frontend_dist/`
4. **Serves**: FastAPI serves both API and static files

### Port Configuration

Railway automatically sets the `PORT` environment variable. The app listens on `0.0.0.0:$PORT`.

## 📁 Project Structure

```
credit-card-optimizer/
├── Dockerfile              # Multi-stage build
├── docker-compose.yml      # Local testing
├── railway.json            # Railway config
├── backend/                # FastAPI backend
│   ├── main.py            # Serves API + static files
│   └── ...
├── frontend/               # Next.js frontend
│   ├── next.config.js     # Static export config
│   └── ...
└── frontend_dist/          # Built frontend (created during build)
```

## 🧪 Local Testing

### Test with Docker Compose

```bash
# Build and run
docker compose up --build

# Visit http://localhost:8000
```

### Test Locally (Development)

```bash
# Terminal 1: Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Terminal 2: Frontend
cd frontend
npm install
npm run dev

# Visit http://localhost:3000
```

## 🔍 Health Check

Railway automatically checks: `GET /health`

Response:
```json
{
  "status": "healthy",
  "service": "credit-card-optimizer",
  "version": "1.0.0"
}
```

## 📊 Monitoring

- **Logs**: View in Railway dashboard
- **Metrics**: CPU, Memory, Network in dashboard
- **Deployments**: Automatic on git push to main branch

## 🐛 Troubleshooting

### Build Fails

1. **Check logs** in Railway dashboard
2. **Verify Dockerfile** is in root directory
3. **Check** that `frontend/package.json` exists
4. **Ensure** `backend/requirements.txt` exists

### Frontend Not Loading

1. **Check** that `frontend_dist/` exists after build
2. **Verify** Next.js build completed successfully
3. **Check** `/health` endpoint works
4. **Review** Railway logs for errors

### API Calls Fail

1. **Verify** API client uses relative paths (`/api/optimizer/recommend`)
2. **Check** that router is included in `main.py`
3. **Test** API directly: `curl https://your-app.railway.app/api/optimizer/cards`

### Port Issues

- Railway sets `PORT` automatically
- App listens on `0.0.0.0:$PORT`
- No manual port configuration needed

## ✅ Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] Railway project created
- [ ] GitHub repo connected
- [ ] Build completes successfully
- [ ] `/health` endpoint returns 200
- [ ] Frontend loads at root URL
- [ ] API calls work from frontend
- [ ] No CORS errors in browser console

## 🔗 URLs

After deployment:
- **App URL**: `https://your-app.railway.app`
- **API**: `https://your-app.railway.app/api/optimizer/recommend`
- **Health**: `https://your-app.railway.app/health`
- **Frontend**: `https://your-app.railway.app/` (same URL!)

## 🎯 Key Features

✅ **Single Container** - Everything in one place  
✅ **No CORS** - Same origin for API and frontend  
✅ **No Env Vars** - Zero configuration needed  
✅ **Auto Deploy** - Push to main = deploy  
✅ **Health Checks** - Automatic monitoring  
✅ **Static Export** - Fast, optimized frontend  

## 📝 Notes

- Frontend is statically exported (no Next.js server needed)
- All API calls use relative paths
- Railway handles SSL/TLS automatically
- Custom domains available in Railway Pro

---

**Need help?** Check Railway docs: https://docs.railway.app

