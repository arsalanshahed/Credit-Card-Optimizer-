# Credit Card Optimizer - Full Stack MVP

A production-ready MVP for intelligent credit card recommendations with CSV-based data, reward calculation engine, and ranking algorithm.

## 🏗️ Project Structure

```
credit-card-optimizer/
├── backend/                 # FastAPI Python service
│   ├── main.py             # FastAPI application
│   ├── api/
│   │   └── optimizer.py    # POST /recommend endpoint
│   ├── services/
│   │   ├── card_loader.py          # CSV parser
│   │   ├── reward_calculator.py    # Reward calculation engine
│   │   └── card_ranker.py          # Ranking algorithm
│   ├── data/
│   │   └── credit_cards.csv        # Card data
│   └── requirements.txt
│
├── frontend/                # Next.js 14 App Router
│   ├── app/
│   │   ├── page.tsx        # Landing page
│   │   ├── optimizer/      # Main tool
│   │   └── dashboard/      # Saved simulations
│   ├── components/
│   │   ├── CardInputForm.tsx
│   │   ├── MultiCardComparisonTable.tsx
│   │   ├── SavingsSimulationChart.tsx
│   │   ├── OfferCard.tsx
│   │   └── DetailedSavingsModal.tsx
│   └── package.json
│
└── shared/                  # Shared types
    └── types/
        └── api.py
```

## 🚀 Quick Start

### Local Development

#### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Backend: http://localhost:8000
API Docs: http://localhost:8000/docs

#### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:3000

### Docker Compose

```bash
docker-compose up --build
```

## 📡 API Endpoints

### `POST /api/optimizer/recommend`

**Request:**
```json
{
  "groceries": 500,
  "travel": 300,
  "gas": 200,
  "dining": 400,
  "online_shopping": 600
}
```

**Response:**
```json
{
  "recommendations": [
    {
      "card_name": "Discover It Cash Back",
      "issuer": "Discover",
      "reward_rate": 0.032,
      "annual_fee": 0,
      "estimated_monthly_rewards": 64.50,
      "estimated_annual_rewards": 774.00,
      "cashback_breakdown": [...]
    }
  ],
  "total_monthly_spend": 2000,
  "best_card": {...},
  "explanation": "..."
}
```

### `GET /api/optimizer/cards`

Returns all cards from CSV.

## 🎯 Features

- **CSV-based card data** - Easy to update and maintain
- **Reward calculator** - Accounts for category caps and annual fees
- **Ranking algorithm** - Optimizes for first-year value
- **Simple UI** - 5 input fields for spending categories
- **Comparison table** - Side-by-side card comparison
- **Charts** - Visual reward breakdowns
- **Detailed modal** - Category-by-category savings breakdown

## 🚢 Deployment

### Backend to Render

1. Push code to GitHub
2. Connect repo to Render
3. Set root directory: `backend`
4. Build: `pip install -r requirements.txt`
5. Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Frontend to Vercel

1. Connect GitHub repo to Vercel
2. Set root directory: `frontend`
3. Add env var: `NEXT_PUBLIC_API_URL=https://your-backend.onrender.com`
4. Deploy

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

## 📊 Data Format

CSV columns:
- `card_name`: Card name
- `issuer`: Bank/issuer
- `base_reward`: Base cashback rate (0.01 = 1%)
- `category_rewards`: JSON string of category rates
- `annual_fee`: Annual fee in dollars
- `signup_bonus`: Signup bonus amount
- `signup_bonus_spend_requirement`: Spending requirement for bonus
- `category_caps`: JSON string of monthly category caps

## 🔧 Configuration

### Environment Variables

**Backend:**
- `PORT`: Server port (auto-set by Render)

**Frontend:**
- `NEXT_PUBLIC_API_URL`: Backend API URL

## 📝 License

MIT License
