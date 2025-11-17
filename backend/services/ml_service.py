"""
ML service for model predictions.
"""
import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Optional, Tuple
from sklearn.preprocessing import OneHotEncoder, StandardScaler

BACKEND_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BACKEND_DIR / "data" / "models"


class MLService:
    """Service for ML model predictions."""
    
    def __init__(self):
        self.model = None
        self.encoder = None
        self.scaler = None
        self.load_models()
    
    def load_models(self):
        """Load trained models."""
        try:
            self.model = joblib.load(MODELS_DIR / "reward_model.pkl")
            self.encoder = joblib.load(MODELS_DIR / "encoder.pkl")
            self.scaler = joblib.load(MODELS_DIR / "scaler.pkl")
        except FileNotFoundError:
            print("Warning: Model files not found")
    
    def predict(self, category: str, amount: float) -> Optional[str]:
        """
        Predict best card using ML model.
        
        Args:
            category: Purchase category
            amount: Transaction amount
        
        Returns:
            Predicted card name or None if model not loaded
        """
        if not self.model or not self.encoder or not self.scaler:
            return None
        
        try:
            df = pd.DataFrame({"category": [category], "amount": [amount]})
            X_cat = self.encoder.transform([[category]])
            X_amt = self.scaler.transform([[amount]])
            X = np.hstack([X_cat, X_amt])
            prediction = self.model.predict(X)[0]
            return prediction
        except Exception as e:
            print(f"ML prediction error: {e}")
            return None
    
    def is_loaded(self) -> bool:
        """Check if models are loaded."""
        return self.model is not None

