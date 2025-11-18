# 🚀 Deployment Guide - Railway (Unified)

This project uses **Railway** for unified deployment. Both backend and frontend run in a single container.

## Quick Start

1. **Go to**: https://railway.app
2. **Click**: "New Project" → "Deploy from GitHub repo"
3. **Select**: Your `Credit-Card-Optimizer-` repository
4. **Deploy**: Railway auto-detects everything!

See [RAILWAY_DEPLOY.md](./RAILWAY_DEPLOY.md) for detailed instructions.

## Local Testing

```bash
docker compose up --build
# Visit http://localhost:8000
```

## Architecture

- **Single Container**: FastAPI + Next.js static files
- **No CORS**: Same origin for everything
- **No Env Vars**: Zero configuration
- **Auto Deploy**: Push to main = deploy

---

**Old deployment methods (Vercel + Render) have been removed. Use Railway for unified deployment.**
