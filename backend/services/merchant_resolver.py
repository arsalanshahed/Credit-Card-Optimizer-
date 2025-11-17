"""
Merchant name normalization and category resolution.
"""
import re
import pandas as pd
from typing import Dict, Any
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BACKEND_DIR / "data"


def normalize_merchant_name(merchant: str) -> str:
    """Normalize merchant name for better matching."""
    merchant = merchant.strip()
    merchant = re.sub(r'^(THE\s+|A\s+)', '', merchant, flags=re.IGNORECASE)
    merchant = re.sub(r'\s+(INC|LLC|CORP|LTD)\.?$', '', merchant, flags=re.IGNORECASE)
    merchant = re.sub(r'[^\w\s-]', '', merchant)
    merchant = ' '.join(merchant.split())
    return merchant


def get_merchant_info_with_fallback(merchant_name: str) -> Dict[str, Any]:
    """Get merchant information with multiple fallback strategies."""
    # Try local CSV first
    merchant_categories_path = DATA_DIR / "merchant_categories.csv"
    if merchant_categories_path.exists():
        try:
            df = pd.read_csv(merchant_categories_path)
            merchant_lower = merchant_name.lower().strip()
            match = df[df["merchant"].str.lower().str.strip() == merchant_lower]
            if not match.empty:
                row = match.iloc[0]
                return {
                    "merchant": merchant_name,
                    "category": row.get("category", "Other"),
                    "mcc_code": str(row.get("mcc_code", "")).zfill(4) if pd.notna(row.get("mcc_code")) else None,
                    "source": "local_csv"
                }
        except Exception:
            pass
    
    # Fallback: Use common merchant mappings
    common_merchants = {
        "chipotle": {"category": "Dining", "mcc_code": "5812"},
        "walmart": {"category": "Groceries", "mcc_code": "5411"},
        "amazon": {"category": "Online Shopping", "mcc_code": "5999"},
        "costco": {"category": "Gas", "mcc_code": "5542"},
        "target": {"category": "Groceries", "mcc_code": "5411"},
        "walgreens": {"category": "Drugstores", "mcc_code": "5912"},
    }
    
    merchant_lower = merchant_name.lower()
    for key, value in common_merchants.items():
        if key in merchant_lower:
            return {
                "merchant": merchant_name,
                "category": value["category"],
                "mcc_code": value["mcc_code"],
                "source": "fallback_mapping"
            }
    
    return {
        "merchant": merchant_name,
        "category": "Other",
        "mcc_code": None,
        "source": "default"
    }


def resolve_merchant_to_category(merchant_name: str) -> Dict[str, Any]:
    """Resolve merchant to category and MCC code."""
    normalized = normalize_merchant_name(merchant_name)
    return get_merchant_info_with_fallback(normalized)

