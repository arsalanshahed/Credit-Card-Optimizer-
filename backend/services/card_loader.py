"""
Load credit card data from CSV file.
"""
import csv
import json
from pathlib import Path
from typing import List, Dict, Any

BACKEND_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BACKEND_DIR / "data"


def load_cards_from_csv() -> List[Dict[str, Any]]:
    """
    Load credit cards from CSV file.
    
    Returns:
        List of card dictionaries with parsed reward structures
    """
    csv_path = DATA_DIR / "credit_cards.csv"
    
    if not csv_path.exists():
        print(f"Warning: {csv_path} not found")
        return []
    
    cards = []
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Parse category_rewards JSON string
                category_rewards = {}
                if row.get('category_rewards'):
                    try:
                        category_rewards = json.loads(row['category_rewards'].replace("'", '"'))
                    except json.JSONDecodeError:
                        pass
                
                # Parse category_caps JSON string
                category_caps = {}
                if row.get('category_caps'):
                    try:
                        category_caps = json.loads(row['category_caps'].replace("'", '"'))
                    except json.JSONDecodeError:
                        pass
                
                card = {
                    'name': row['card_name'],
                    'issuer': row.get('issuer', 'Unknown'),
                    'base_reward': float(row.get('base_reward', 0.01)),
                    'category_rewards': category_rewards,
                    'annual_fee': float(row.get('annual_fee', 0)),
                    'signup_bonus': float(row.get('signup_bonus', 0)),
                    'signup_bonus_spend_requirement': float(row.get('signup_bonus_spend_requirement', 0)),
                    'category_caps': category_caps,
                }
                cards.append(card)
        
        return cards
    except Exception as e:
        print(f"Error loading cards from CSV: {e}")
        return []


def get_card_by_name(card_name: str) -> Dict[str, Any] | None:
    """Get a specific card by name."""
    cards = load_cards_from_csv()
    return next((c for c in cards if c['name'] == card_name), None)


