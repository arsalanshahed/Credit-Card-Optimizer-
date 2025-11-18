# ✅ Railway Deployment Checklist

## Pre-Deployment

- [x] Dockerfile created with multi-stage build
- [x] docker-compose.yml for local testing
- [x] Next.js configured for static export
- [x] Backend modified to serve static files
- [x] API client uses relative paths
- [x] Health endpoint added (`/health`)
- [x] Railway config created (`railway.json`)
- [x] Old deployment configs removed

## Local Testing

- [ ] Run `docker compose up --build`
- [ ] Visit `http://localhost:8000`
- [ ] Test frontend loads correctly
- [ ] Test API: `POST /api/optimizer/recommend`
- [ ] Test health: `GET /health`
- [ ] Verify no CORS errors
- [ ] Test all frontend routes work

## Railway Deployment

- [ ] Create Railway account
- [ ] Connect GitHub repository
- [ ] Create new project
- [ ] Select repository: `Credit-Card-Optimizer-`
- [ ] Verify Railway auto-detects Dockerfile
- [ ] Click "Deploy"
- [ ] Wait for build to complete
- [ ] Check build logs for errors

## Post-Deployment Verification

- [ ] Visit deployed URL
- [ ] Frontend loads at root URL
- [ ] Health check works: `GET /health`
- [ ] API endpoint works: `GET /api/optimizer/cards`
- [ ] Frontend can call API (no CORS errors)
- [ ] Test full flow: Enter spend → Get recommendations
- [ ] Check Railway logs for any errors
- [ ] Verify all routes work (/, /optimizer, /dashboard)

## Troubleshooting

If build fails:
- [ ] Check Railway build logs
- [ ] Verify Dockerfile syntax
- [ ] Check that all files exist
- [ ] Verify package.json and requirements.txt

If frontend doesn't load:
- [ ] Check that `frontend_dist/` was created
- [ ] Verify Next.js build completed
- [ ] Check backend logs for static file serving

If API doesn't work:
- [ ] Test API directly with curl
- [ ] Check that router is included
- [ ] Verify CSV file exists in backend/data/

## Success Criteria

✅ Single URL serves everything  
✅ No CORS errors  
✅ Frontend loads correctly  
✅ API calls work  
✅ Health check passes  
✅ All routes functional  

---

**Once all items are checked, your deployment is complete!** 🎉

