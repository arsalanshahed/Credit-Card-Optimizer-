"""
Shared API types and interfaces for backend and frontend.
"""
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


# Request Models
class RecommendationRequest(BaseModel):
    """Request model for credit card recommendation."""
    merchant: str = Field(..., description="Merchant name")
    amount: float = Field(..., gt=0, description="Transaction amount in dollars")


# Response Models
class CardInfo(BaseModel):
    """Information about a credit card reward."""
    card_name: str
    reward_amount: float
    reward_rate: float


class RecommendationResponse(BaseModel):
    """Response model for credit card recommendation."""
    best_card: str
    reward_value: float
    merchant_category: str
    mcc_code: Optional[str] = None
    alternatives_ranked: List[CardInfo]
    confidence: float
    explanation: str


class MerchantInfoResponse(BaseModel):
    """Response model for merchant information."""
    merchant: str
    category: str
    mcc_code: Optional[str]
    source: str
    mcc_details: Optional[Dict[str, Any]] = None


class Card(BaseModel):
    """Credit card model."""
    name: str
    base_reward: float
    category_rewards: Dict[str, float] = Field(default_factory=dict)


# Type aliases for TypeScript compatibility
CardDict = Dict[str, Any]
RewardResult = Dict[str, Any]

