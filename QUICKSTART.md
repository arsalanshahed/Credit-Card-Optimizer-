# Quick Start Guide

## 🚀 Run Locally

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend: http://localhost:8000

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:3000

## 🧪 Test the API

```bash
curl -X POST "http://localhost:8000/api/optimizer/recommend" \
     -H "Content-Type: application/json" \
     -d '{
       "groceries": 500,
       "travel": 300,
       "gas": 200,
       "dining": 400,
       "online_shopping": 600
     }'
```

## 📊 CSV Data Format

Edit `backend/data/credit_cards.csv` to add/update cards:

```csv
card_name,issuer,base_reward,category_rewards,annual_fee,signup_bonus,signup_bonus_spend_requirement,category_caps
Your Card,Bank,0.01,"{""Dining"": 0.03}",0,200,1000,"{}"
```

## 🚢 Deploy

See [DEPLOYMENT.md](DEPLOYMENT.md) for Render + Vercel deployment.


