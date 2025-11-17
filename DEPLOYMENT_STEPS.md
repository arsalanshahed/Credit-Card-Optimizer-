# 🚀 Deployment Steps - Follow These Exactly

## ✅ Pre-Deployment Checklist

- [x] Code pushed to GitHub: `https://github.com/arsalanshahed/Credit-Card-Optimizer-.git`
- [x] `render.yaml` configured
- [x] `vercel.json` configured
- [x] CORS updated for production

---

## 📋 Step-by-Step Deployment

### PART 1: Deploy Backend to Render

1. **Open Render Dashboard**
   ```
   https://dashboard.render.com
   ```

2. **Click "New +" → "Web Service"**

3. **Connect GitHub Repository**
   - Select: `Credit-Card-Optimizer-`
   - Click "Connect"

4. **Fill in Configuration**:
   ```
   Name: credit-card-optimizer-backend
   Environment: Python 3
   Region: (choose closest)
   Branch: main
   Root Directory: backend
   Build Command: pip install -r requirements.txt
   Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
   Instance Type: Free
   ```

5. **Add Environment Variable**:
   - Key: `PYTHON_VERSION`
   - Value: `3.11.6`

6. **Click "Create Web Service"**

7. **Wait for Deployment** (3-5 minutes)
   - Watch the logs
   - Look for: "Your service is live"

8. **Copy Your Backend URL**
   - Example: `https://credit-card-optimizer-backend.onrender.com`
   - **SAVE THIS URL** - you'll need it for frontend!

---

### PART 2: Deploy Frontend to Vercel

1. **Open Vercel Dashboard**
   ```
   https://vercel.com/dashboard
   ```

2. **Click "Add New..." → "Project"**

3. **Import GitHub Repository**
   - Select: `Credit-Card-Optimizer-`
   - Click "Import"

4. **Configure Project**:
   ```
   Framework Preset: Next.js (auto-detected)
   Root Directory: frontend
   Build Command: npm run build (auto)
   Output Directory: .next (auto)
   Install Command: npm install (auto)
   ```

5. **Add Environment Variable**:
   - Key: `NEXT_PUBLIC_API_URL`
   - Value: `https://your-backend-url.onrender.com`
     - ⚠️ **Replace with your actual Render backend URL from Part 1!**

6. **Click "Deploy"**

7. **Wait for Deployment** (2-3 minutes)

8. **Copy Your Frontend URL**
   - Example: `https://credit-card-optimizer.vercel.app`

---

### PART 3: Update CORS (If Needed)

If you see CORS errors in browser console:

1. **Go back to Render Dashboard**
2. **Select your backend service**
3. **Go to "Environment" tab**
4. **Add Environment Variable**:
   - Key: `ENVIRONMENT`
   - Value: `production`
5. **Redeploy** (or it will auto-redeploy)

---

## 🧪 Test Your Deployment

### Test Backend:
1. Visit: `https://your-backend.onrender.com/docs`
2. Should see FastAPI Swagger UI
3. Try: `POST /api/optimizer/recommend` with:
   ```json
   {
     "groceries": 500,
     "travel": 300,
     "gas": 200,
     "dining": 400,
     "online_shopping": 600
   }
   ```

### Test Frontend:
1. Visit: `https://your-app.vercel.app/optimizer`
2. Enter spending amounts
3. Click "Find Best Cards"
4. Should see recommendations!

---

## 🎯 Your Live URLs

After deployment, you'll have:

- **Frontend**: `https://credit-card-optimizer.vercel.app`
- **Backend**: `https://credit-card-optimizer-backend.onrender.com`
- **API Docs**: `https://credit-card-optimizer-backend.onrender.com/docs`

---

## 🆘 Common Issues

### Backend won't start
- Check Render logs
- Verify `backend/main.py` exists
- Ensure `requirements.txt` is in `backend/` directory

### Frontend can't connect to backend
- Verify `NEXT_PUBLIC_API_URL` is set correctly in Vercel
- Check that backend URL doesn't have trailing slash
- Ensure backend is running (check Render dashboard)

### CORS errors
- Add `ENVIRONMENT=production` to Render environment variables
- Or manually update `allow_origins` in `backend/main.py`

---

## ✅ Success Checklist

- [ ] Backend deployed and accessible
- [ ] Frontend deployed and accessible
- [ ] API calls work from frontend
- [ ] No CORS errors
- [ ] Recommendations display correctly

**You're done! 🎉**

