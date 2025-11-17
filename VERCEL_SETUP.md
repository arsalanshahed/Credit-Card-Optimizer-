# 🔧 Vercel Deployment Setup - IMPORTANT

## The Issue
Vercel is trying to run `cd frontend` but can't find the directory. This happens because the Root Directory isn't configured correctly.

## Solution: Configure in Vercel Dashboard

**You MUST set the Root Directory in Vercel project settings. The vercel.json file alone is not enough.**

### Step-by-Step Fix:

1. **Go to Vercel Dashboard**
   - https://vercel.com/dashboard
   - Click on your project: `credit-card-optimizer`

2. **Go to Settings**
   - Click "Settings" tab
   - Click "General" in the left sidebar

3. **Set Root Directory**
   - Scroll down to "Root Directory"
   - Click "Edit" button
   - Enter: `frontend`
   - Click "Save"

4. **Verify Build Settings**
   - Still in Settings → General
   - Check "Build and Output Settings"
   - Framework Preset should be: `Next.js`
   - Build Command: `npm run build` (auto-detected)
   - Output Directory: `.next` (auto-detected)
   - Install Command: `npm install` (auto-detected)

5. **Set Environment Variable**
   - Go to Settings → "Environment Variables"
   - Add: `NEXT_PUBLIC_API_URL` = `https://your-backend-url.onrender.com`
   - Make sure it's set for "Production", "Preview", and "Development"

6. **Redeploy**
   - Go to "Deployments" tab
   - Click the "..." menu on the latest deployment
   - Click "Redeploy"
   - OR push a new commit to trigger auto-deploy

## Alternative: If Root Directory Setting Doesn't Work

If you can't set Root Directory, we can use a different approach:

1. **Delete the project in Vercel**
2. **Re-import with these settings:**
   - When importing, manually set:
     - Root Directory: `frontend`
     - Framework: `Next.js`
   - This should work better than trying to change it after import

## Current Configuration

- `vercel.json` has been moved to `frontend/vercel.json`
- Root `vercel.json` has been removed
- All build commands assume you're already in the `frontend` directory

## After Setting Root Directory

Once Root Directory is set to `frontend`:
- Vercel will automatically be in the `frontend` directory
- All commands will run from there
- Build should succeed

## Still Having Issues?

If the error persists:
1. Check that Root Directory is actually saved (refresh the page)
2. Try deleting and re-importing the project
3. Check Vercel build logs for the exact error message

