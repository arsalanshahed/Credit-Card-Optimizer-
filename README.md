# 💳 Credit Card Optimizer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Next.js](https://img.shields.io/badge/Next.js-14-black?logo=next.js)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green?logo=fastapi)
![TypeScript](https://img.shields.io/badge/TypeScript-5.3-blue?logo=typescript)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.4-38bdf8?logo=tailwind-css)
![Railway](https://img.shields.io/badge/Deployed%20on-Railway-0B0D0E?logo=railway)

**Intelligent credit card recommendation engine that maximizes rewards based on your spending patterns**

[Live Demo](#-live-demo) • [Features](#-features) • [Tech Stack](#-tech-stack) • [Deployment](#-deployment) • [API Documentation](#-api-documentation)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [API Documentation](#-api-documentation)
- [Deployment](#-deployment)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

## 🎯 Overview

Credit Card Optimizer is a full-stack web application that helps users maximize their credit card rewards by analyzing spending patterns and recommending the optimal card. The system uses a rule-augmented algorithm that considers category-specific rewards, annual fees, signup bonuses, and spending caps to provide personalized recommendations.

### Key Highlights

- 🚀 **Production-Ready MVP** - Fully functional with real-world data
- 📊 **Data-Driven** - CSV-based card database with 8+ major credit cards
- 🎨 **Modern UI** - Premium FinTech design with glassmorphism effects
- 🔄 **Real-Time** - Instant recommendations based on spending input
- 📈 **Analytics** - Visual breakdowns and savings simulations
- 🐳 **Unified Deployment** - Single-container architecture on Railway

## ✨ Features

### Core Functionality
- **Smart Recommendations** - Algorithm ranks cards by first-year value
- **Category Analysis** - Optimizes for groceries, travel, gas, dining, online shopping
- **Reward Calculation** - Accounts for category caps, annual fees, and signup bonuses
- **Comparison Tools** - Side-by-side card comparison with detailed breakdowns
- **Savings Simulation** - Visual charts showing estimated monthly/annual rewards

### User Experience
- **Intuitive Interface** - 5 simple input fields for monthly spending
- **Detailed Modals** - Category-by-category savings breakdown
- **Responsive Design** - Works seamlessly on desktop and mobile
- **Fast Performance** - Static export for optimal loading times
- **No Configuration** - Zero environment variables needed

### Technical Excellence
- **Unified Deployment** - Single container eliminates CORS issues
- **Type Safety** - Full TypeScript coverage
- **API Documentation** - Auto-generated Swagger/OpenAPI docs
- **Health Monitoring** - Built-in health check endpoints
- **Scalable Architecture** - Easy to extend with new cards or features

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern, fast Python web framework
- **Python 3.11** - Latest Python features
- **Pandas** - Data processing and CSV parsing
- **Uvicorn** - ASGI server for production

### Frontend
- **Next.js 14** - React framework with App Router
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first styling
- **shadcn/ui** - High-quality React components
- **Framer Motion** - Smooth animations
- **Recharts** - Data visualization
- **Zustand** - Lightweight state management

### Infrastructure
- **Docker** - Containerization
- **Railway** - Unified deployment platform
- **GitHub** - Version control and CI/CD

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│         Railway Container               │
│                                         │
│  ┌──────────────────────────────────┐  │
│  │      FastAPI Backend             │  │
│  │  - /api/optimizer/recommend     │  │
│  │  - /api/optimizer/cards         │  │
│  │  - /health                      │  │
│  └──────────────────────────────────┘  │
│                                         │
│  ┌──────────────────────────────────┐  │
│  │   Next.js Static Frontend        │  │
│  │   - Served from /                │  │
│  │   - SPA routing                  │  │
│  └──────────────────────────────────┘  │
│                                         │
│  Single Domain • No CORS • Zero Config │
└─────────────────────────────────────────┘
```

### Data Flow

1. **User Input** → Frontend collects spending categories
2. **API Request** → POST to `/api/optimizer/recommend`
3. **Data Processing** → Backend loads cards from CSV
4. **Reward Calculation** → Algorithm computes rewards per card
5. **Ranking** → Cards sorted by estimated value
6. **Response** → Frontend displays recommendations with charts

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- Docker Desktop (for unified deployment)

### Option 1: Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/Credit-Card-Optimizer-.git
cd credit-card-optimizer

# Start the application
docker compose up --build

# Visit http://localhost:8000
```

### Option 2: Local Development

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend (new terminal)
cd frontend
npm install
npm run dev

# Visit http://localhost:3000
```

## 📡 API Documentation

### Endpoints

#### `POST /api/optimizer/recommend`

Get personalized credit card recommendations based on spending.

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
      "cashback_breakdown": [
        {
          "category": "Groceries",
          "amount": 500,
          "reward_earned": 25.00,
          "rate": 0.05
        }
      ]
    }
  ],
  "total_monthly_spend": 2000,
  "best_card": {...},
  "explanation": "The Discover It Cash Back is recommended..."
}
```

#### `GET /api/optimizer/cards`

Retrieve all available credit cards from the database.

#### `GET /health`

Health check endpoint for monitoring.

### Interactive API Docs

When running locally, visit `http://localhost:8000/docs` for interactive Swagger documentation.

## 🚢 Deployment

### Railway (Production)

This project is configured for one-click deployment on Railway:

1. **Fork/Clone** this repository
2. **Go to** [Railway](https://railway.app)
3. **Click** "New Project" → "Deploy from GitHub repo"
4. **Select** your repository
5. **Deploy** - Railway auto-detects the Dockerfile!

**Why Railway?**
- ✅ Single container (no CORS issues)
- ✅ Zero configuration (no env vars needed)
- ✅ Automatic SSL/TLS
- ✅ Health checks built-in
- ✅ Free tier available

See [RAILWAY_DEPLOY.md](./RAILWAY_DEPLOY.md) for detailed instructions.

## 📁 Project Structure

```
credit-card-optimizer/
├── backend/                    # FastAPI application
│   ├── main.py                # Main FastAPI app + static serving
│   ├── api/
│   │   └── optimizer.py       # Recommendation endpoints
│   ├── services/
│   │   ├── card_loader.py     # CSV parser
│   │   ├── reward_calculator.py # Reward engine
│   │   └── card_ranker.py     # Ranking algorithm
│   ├── data/
│   │   └── credit_cards.csv   # Card database
│   └── requirements.txt
│
├── frontend/                   # Next.js application
│   ├── app/
│   │   ├── page.tsx          # Landing page
│   │   ├── optimizer/        # Main tool
│   │   └── dashboard/        # Analytics
│   ├── components/
│   │   ├── CardInputForm.tsx
│   │   ├── MultiCardComparisonTable.tsx
│   │   ├── SavingsSimulationChart.tsx
│   │   └── DetailedSavingsModal.tsx
│   └── lib/
│       ├── api-client.ts     # API integration
│       └── store.ts         # State management
│
├── Dockerfile                  # Multi-stage build
├── docker-compose.yml          # Local testing
├── railway.json                # Railway config
└── README.md                   # This file
```

## 🎓 Learning Outcomes

This project demonstrates:

- **Full-Stack Development** - End-to-end application development
- **API Design** - RESTful API with proper error handling
- **Data Processing** - CSV parsing and reward calculations
- **Algorithm Design** - Card ranking and optimization logic
- **Modern Frontend** - React, TypeScript, and responsive design
- **DevOps** - Docker, containerization, and cloud deployment
- **Production Best Practices** - Health checks, error handling, documentation

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📊 Data Format

The card database (`backend/data/credit_cards.csv`) uses the following format:

| Column | Description | Example |
|--------|-------------|---------|
| `card_name` | Card name | "Discover It Cash Back" |
| `issuer` | Bank/issuer | "Discover" |
| `base_reward` | Base cashback rate | 0.01 (1%) |
| `category_rewards` | JSON of category rates | `{"Groceries": 0.05}` |
| `annual_fee` | Annual fee in dollars | 0 |
| `signup_bonus` | Signup bonus amount | 200 |
| `category_caps` | JSON of monthly caps | `{"Groceries": 1500}` |

## 🔧 Configuration

**No environment variables required!** The unified deployment uses relative paths for API calls.

Optional (for local development):
- `PORT`: Server port (default: 8000)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Portfolio: [Your Website](https://yourwebsite.com)

## 🙏 Acknowledgments

- Credit card data sourced from public information
- UI components from [shadcn/ui](https://ui.shadcn.com)
- Icons from [Lucide](https://lucide.dev)

---

<div align="center">

**⭐ If you found this project helpful, please give it a star! ⭐**

Made with ❤️ using FastAPI, Next.js, and TypeScript

</div>
