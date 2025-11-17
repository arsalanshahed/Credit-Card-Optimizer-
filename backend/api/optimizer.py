"""
API endpoints for credit card optimizer.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Any
import sys
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BACKEND_DIR))

from services.card_loader import load_cards_from_csv
from services.card_ranker import rank_cards, generate_explanation

router = APIRouter(prefix="/api/optimizer", tags=["optimizer"])


class SpendRequest(BaseModel):
    groceries: float = 0
    travel: float = 0
    gas: float = 0
    dining: float = 0
    online_shopping: float = 0


class CardRecommendation(BaseModel):
    card_name: str
    issuer: str
    reward_rate: float
    annual_fee: float
    estimated_monthly_rewards: float
    estimated_annual_rewards: float
    cashback_breakdown: List[Dict[str, Any]]


class RecommendationResponse(BaseModel):
    recommendations: List[CardRecommendation]
    total_monthly_spend: float
    best_card: CardRecommendation
    explanation: str = ""


@router.get("/cards")
async def get_cards():
    """Get all available credit cards from CSV."""
    cards = load_cards_from_csv()
    return {"cards": cards, "count": len(cards)}


@router.post("/recommend", response_model=RecommendationResponse)
async def recommend_cards(request: SpendRequest):
    """
    Recommend credit cards based on spending categories.
    Uses CSV data and ranking algorithm.
    """
    try:
        spend_dict = request.dict()
        total_spend = sum(spend_dict.values())
        
        if total_spend == 0:
            raise HTTPException(status_code=400, detail="Total spend must be greater than 0")
        
        # Load cards from CSV
        cards = load_cards_from_csv()
        
        if not cards:
            raise HTTPException(status_code=500, detail="No cards available")
        
        # Rank cards
        ranked_cards = rank_cards(cards, spend_dict)
        
        # Convert to response format
        recommendations = []
        for ranked_card in ranked_cards:
            recommendations.append(CardRecommendation(
                card_name=ranked_card['card_name'],
                issuer=ranked_card['issuer'],
                reward_rate=ranked_card['overall_rate'],
                annual_fee=ranked_card['effective_annual_fee'],
                estimated_monthly_rewards=ranked_card['reward_value_monthly'],
                estimated_annual_rewards=ranked_card['reward_value_yearly'],
                cashback_breakdown=ranked_card['category_breakdown']
            ))
        
        # Generate explanation
        best_card_data = ranked_cards[0] if ranked_cards else None
        explanation = generate_explanation(best_card_data, spend_dict) if best_card_data else "No recommendations available"
        
        return RecommendationResponse(
            recommendations=recommendations,
            total_monthly_spend=total_spend,
            best_card=recommendations[0] if recommendations else None,
            explanation=explanation
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

