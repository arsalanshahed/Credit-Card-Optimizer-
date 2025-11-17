"""
FastAPI backend for credit card optimization.
"""
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import sys

# Add shared types to path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "shared"))

from services.reward_optimizer import RewardOptimizer
from services.ml_service import MLService
from services.api_clients import fetch_mcc_info
from api.optimizer import router as optimizer_router

# Import shared types if available, otherwise use local types
try:
    from shared.types.api import (
        RecommendationRequest,
        RecommendationResponse,
        MerchantInfoResponse,
        Card
    )
except ImportError:
    # Fallback: define minimal types locally
    from pydantic import BaseModel
    from typing import List, Optional, Dict, Any
    
    class RecommendationRequest(BaseModel):
        merchant: str
        amount: float
    
    class RecommendationResponse(BaseModel):
        best_card: str
        reward_amount: float
        confidence: float
        explanation: str
    
    class MerchantInfoResponse(BaseModel):
        merchant: str
        category: str
        mcc_code: Optional[str] = None
        source: str = "unknown"
        mcc_details: Optional[Dict[str, Any]] = None
    
    class Card(BaseModel):
        name: str
        issuer: str
        annual_fee: float
        base_reward: float
        category_rewards: Dict[str, float]

app = FastAPI(
    title="Credit Card Optimizer API",
    description="Real-time credit card recommendation engine",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(optimizer_router)

# Initialize services
reward_optimizer = RewardOptimizer()
ml_service = MLService()


@app.get("/")
def root():
    """API information."""
    return {
        "message": "Credit Card Optimizer API",
        "version": "1.0.0",
        "endpoints": {
            "POST /recommend": "Get credit card recommendation",
            "GET /cards": "List all available credit cards",
            "GET /merchant-info/{merchant_name}": "Get merchant category and MCC info"
        },
        "model_loaded": ml_service.is_loaded()
    }


@app.get("/favicon.ico")
def favicon():
    """Handle favicon requests."""
    return Response(status_code=204)


@app.get("/cards")
def get_cards():
    """Get all available credit cards from CSV."""
    from services.card_loader import load_cards_from_csv
    cards = load_cards_from_csv()
    return {"cards": cards, "count": len(cards)}


@app.get("/merchant-info/{merchant_name}", response_model=MerchantInfoResponse)
def get_merchant_info(merchant_name: str):
    """Get merchant information including category and MCC code."""
    from services.merchant_resolver import resolve_merchant_to_category
    
    merchant_info = resolve_merchant_to_category(merchant_name)
    
    # Fetch MCC details if available
    mcc_details = None
    if merchant_info.get("mcc_code"):
        mcc_details = fetch_mcc_info(merchant_info["mcc_code"])
    
    return MerchantInfoResponse(
        merchant=merchant_name,
        category=merchant_info["category"],
        mcc_code=merchant_info.get("mcc_code"),
        source=merchant_info.get("source", "unknown"),
        mcc_details=mcc_details
    )


@app.post("/recommend", response_model=RecommendationResponse)
def recommend(request: RecommendationRequest):
    """Recommend the best credit card for a transaction."""
    try:
        # Get ML prediction if available
        ml_prediction = None
        confidence = 0.85
        
        if ml_service.is_loaded():
            from services.merchant_resolver import resolve_merchant_to_category
            merchant_info = resolve_merchant_to_category(request.merchant)
            ml_prediction = ml_service.predict(
                merchant_info["category"],
                request.amount
            )
        
        # Optimize rewards
        result = reward_optimizer.optimize(
            merchant=request.merchant,
            amount=request.amount,
            ml_prediction=ml_prediction,
            confidence=confidence
        )
        
        return RecommendationResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

