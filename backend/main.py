"""
FastAPI backend for credit card optimization.
Unified deployment: serves both API and frontend static files.
"""
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import sys
import os

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
    title="Credit Card Optimizer",
    description="Unified credit card recommendation engine with frontend",
    version="1.0.0"
)

# CORS middleware - minimal since everything is same-origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Same origin in production, but allow for flexibility
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(optimizer_router)

# Initialize services
reward_optimizer = RewardOptimizer()
ml_service = MLService()

# Mount static files for frontend (must be before catch-all route)
FRONTEND_DIST = Path(__file__).parent.parent / "frontend_dist"
if FRONTEND_DIST.exists():
    # Serve Next.js static assets
    static_dir = FRONTEND_DIST / "_next" / "static"
    if static_dir.exists():
        app.mount("/_next/static", StaticFiles(directory=str(static_dir)), name="static")
    
    # Serve other static files
    for static_path in ["images", "favicon.ico"]:
        static_file = FRONTEND_DIST / static_path
        if static_file.exists():
            if static_file.is_file():
                @app.get(f"/{static_path}")
                def serve_static_file():
                    return FileResponse(str(static_file))
            else:
                app.mount(f"/{static_path}", StaticFiles(directory=str(static_file)), name=static_path)


@app.get("/health")
def health_check():
    """Health check endpoint for Railway."""
    return {
        "status": "healthy",
        "service": "credit-card-optimizer",
        "version": "1.0.0"
    }


@app.get("/")
def root():
    """Serve frontend index.html or API info."""
    index_path = FRONTEND_DIST / "index.html"
    if index_path.exists():
        return FileResponse(str(index_path))
    return {
        "message": "Credit Card Optimizer API",
        "version": "1.0.0",
        "endpoints": {
            "POST /api/optimizer/recommend": "Get credit card recommendation",
            "GET /api/optimizer/cards": "List all available credit cards",
            "GET /health": "Health check"
        }
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


# Catch-all route for frontend SPA routing (must be last)
@app.get("/{full_path:path}")
def serve_frontend(full_path: str):
    """Serve frontend routes for SPA navigation."""
    # Don't serve API routes
    if full_path.startswith("api/") or full_path.startswith("_next/") or full_path in ["health", "favicon.ico"]:
        raise HTTPException(status_code=404, detail="Not found")
    
    # Try to serve the requested file
    requested_file = FRONTEND_DIST / full_path
    if requested_file.exists() and requested_file.is_file():
        return FileResponse(str(requested_file))
    
    # Fallback to index.html for SPA routes
    index_path = FRONTEND_DIST / "index.html"
    if index_path.exists():
        return FileResponse(str(index_path))
    
    raise HTTPException(status_code=404, detail="Not found")


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

