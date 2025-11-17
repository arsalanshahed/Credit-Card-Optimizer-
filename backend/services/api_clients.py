"""
API clients for external data sources.
"""
import requests
from typing import Optional, Dict, Any


def fetch_mcc_info(mcc_code: str) -> Optional[Dict[str, Any]]:
    """Fetch MCC code information from mcc.codes API."""
    try:
        url = f"https://mcc.codes/api/mcc/{mcc_code}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
        return None
    except requests.exceptions.RequestException:
        return None

