"""
Reward optimization service for credit card recommendations.
"""
from typing import Dict, List, Optional
from pathlib import Path
import sys

# Add backend to path
BACKEND_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BACKEND_DIR))

from services.card_loader import load_cards_from_csv
from services.merchant_resolver import resolve_merchant_to_category


class RewardOptimizer:
    """Service for optimizing credit card rewards."""
    
    def __init__(self):
        self.cards = load_cards_from_csv()
    
    def optimize(
        self,
        merchant: str,
        amount: float,
        ml_prediction: Optional[str] = None,
        confidence: float = 0.85
    ) -> Dict:
        """
        Optimize reward by finding the best credit card.
        
        Args:
            merchant: Merchant name
            amount: Transaction amount
            ml_prediction: Optional ML model prediction
            confidence: Confidence score
        
        Returns:
            Dictionary with optimization results
        """
        # Resolve merchant to category
        merchant_info = resolve_merchant_to_category(merchant)
        category = merchant_info["category"]
        mcc_code = merchant_info.get("mcc_code")
        
        # Evaluate all cards
        all_results = evaluate_all_cards(category, amount)
        
        if not all_results:
            raise ValueError("No cards available")
        
        # Determine best card
        rule_best = all_results[0]["card_name"]
        
        if ml_prediction:
            # Use ML prediction if available
            ml_result = next(
                (r for r in all_results if r["card_name"] == ml_prediction),
                None
            )
            if ml_result:
                best_card = ml_prediction
                if ml_prediction == rule_best:
                    confidence = 0.95
                    explanation = f"ML model and rule engine both recommend {best_card} for {category} purchases"
                else:
                    confidence = 0.75
                    explanation = f"ML model recommends {best_card}, rule engine recommends {rule_best}. Using ML prediction."
            else:
                best_card = rule_best
                confidence = 0.85
                explanation = f"Rule engine recommends {best_card} for {category} purchases"
        else:
            best_card = rule_best
            confidence = 0.85
            explanation = f"Rule engine recommends {best_card} for {category} purchases"
        
        # Get best card details
        best_card_info = next(
            (c for c in all_results if c["card_name"] == best_card),
            all_results[0]
        )
        
        # Prepare alternatives
        alternatives = [
            {
                "card_name": result["card_name"],
                "reward_amount": result["reward_amount"],
                "reward_rate": result["reward_rate"]
            }
            for result in all_results
            if result["card_name"] != best_card
        ]
        
        return {
            "best_card": best_card,
            "reward_value": best_card_info["reward_amount"],
            "merchant_category": category,
            "mcc_code": mcc_code,
            "alternatives_ranked": alternatives,
            "confidence": confidence,
            "explanation": explanation
        }
    
    def get_all_cards(self) -> List[Dict]:
        """Get all available credit cards."""
        return self.cards
    
    def compare_cards(self, category: str, amount: float) -> List[Dict]:
        """Compare all cards for a given transaction."""
        return evaluate_all_cards(category, amount)

