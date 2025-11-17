"""
Rule engine for computing credit card rewards based on card rules.
"""
import json
from typing import Dict, List
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BACKEND_DIR / "data"


def load_card_rules() -> List[Dict]:
    """Load credit card reward rules from JSON (fallback)."""
    cards_path = DATA_DIR / "cards.json"
    try:
        with open(cards_path, 'r') as f:
            data = json.load(f)
        return data.get("cards", [])
    except FileNotFoundError:
        # Fallback to CSV loader
        from services.card_loader import load_cards_from_csv
        return load_cards_from_csv()
    except json.JSONDecodeError as e:
        print(f"Error parsing cards.json: {e}")
        from services.card_loader import load_cards_from_csv
        return load_cards_from_csv()


def compute_reward(card: Dict, category: str, amount: float) -> float:
    """Compute reward for a card given category and amount."""
    category_rewards = card.get("category_rewards", {})
    if category in category_rewards:
        return amount * category_rewards[category]
    base_reward = card.get("base_reward", 0.01)
    return amount * base_reward


def get_reward_rate(card: Dict, category: str) -> float:
    """Get the reward rate for a card and category."""
    category_rewards = card.get("category_rewards", {})
    if category in category_rewards:
        return category_rewards[category]
    return card.get("base_reward", 0.01)


def evaluate_all_cards(category: str, amount: float) -> List[Dict]:
    """Evaluate all cards for a given transaction."""
    cards = load_card_rules()
    results = []
    for card in cards:
        reward = compute_reward(card, category, amount)
        rate = get_reward_rate(card, category)
        results.append({
            "card_name": card["name"],
            "reward_amount": round(reward, 2),
            "reward_rate": rate,
            "card_data": card
        })
    results.sort(key=lambda x: x["reward_amount"], reverse=True)
    return results

