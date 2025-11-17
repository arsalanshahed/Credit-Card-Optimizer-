"""
Reward calculation engine for credit cards.
"""
from typing import Dict, List, Any, Tuple


def calculate_reward(
    card: Dict[str, Any],
    category: str,
    amount: float
) -> Tuple[float, float]:
    """
    Calculate reward for a specific category and amount.
    Accounts for category caps.
    
    Args:
        card: Card dictionary
        category: Purchase category
        amount: Transaction amount
    
    Returns:
        Tuple of (reward_amount, effective_rate)
    """
    # Check category-specific reward
    category_rewards = card.get('category_rewards', {})
    category_caps = card.get('category_caps', {})
    
    if category in category_rewards:
        rate = category_rewards[category]
        # Apply category cap if exists
        if category in category_caps:
            capped_amount = min(amount, category_caps[category])
            capped_reward = capped_amount * rate
            # Remaining amount uses base rate
            remaining_amount = max(0, amount - category_caps[category])
            base_reward = remaining_amount * card.get('base_reward', 0.01)
            total_reward = capped_reward + base_reward
            effective_rate = total_reward / amount if amount > 0 else 0
            return total_reward, effective_rate
        else:
            return amount * rate, rate
    
    # Fall back to base reward
    base_reward = card.get('base_reward', 0.01)
    return amount * base_reward, base_reward


def calculate_total_rewards(
    card: Dict[str, Any],
    spend: Dict[str, float]
) -> Dict[str, Any]:
    """
    Calculate total rewards for a card given spending across categories.
    
    Args:
        card: Card dictionary
        spend: Dictionary of category -> monthly spend
    
    Returns:
        Dictionary with reward breakdown
    """
    monthly_rewards = 0
    category_breakdown = []
    
    # Map frontend categories to backend categories
    category_map = {
        'groceries': 'Groceries',
        'travel': 'Travel',
        'gas': 'Gas',
        'dining': 'Dining',
        'online_shopping': 'Online Shopping',
    }
    
    for frontend_category, amount in spend.items():
        if amount > 0:
            backend_category = category_map.get(frontend_category, frontend_category.title())
            reward, effective_rate = calculate_reward(card, backend_category, amount)
            monthly_rewards += reward
            
            category_breakdown.append({
                'category': backend_category,
                'amount': round(reward, 2),
                'rate': effective_rate,
                'spend': amount
            })
    
    annual_rewards = monthly_rewards * 12
    effective_annual_fee = card.get('annual_fee', 0)
    net_annual_rewards = annual_rewards - effective_annual_fee
    
    # Calculate overall reward rate
    total_spend = sum(spend.values())
    overall_rate = monthly_rewards / total_spend if total_spend > 0 else 0
    
    return {
        'monthly_rewards': round(monthly_rewards, 2),
        'annual_rewards': round(annual_rewards, 2),
        'net_annual_rewards': round(net_annual_rewards, 2),
        'effective_annual_fee': effective_annual_fee,
        'overall_rate': overall_rate,
        'category_breakdown': category_breakdown,
    }


def calculate_signup_bonus_value(
    card: Dict[str, Any],
    total_monthly_spend: float
) -> Dict[str, Any]:
    """
    Calculate signup bonus value and eligibility.
    
    Args:
        card: Card dictionary
        total_monthly_spend: Total monthly spending
    
    Returns:
        Dictionary with signup bonus information
    """
    signup_bonus = card.get('signup_bonus', 0)
    spend_requirement = card.get('signup_bonus_spend_requirement', 0)
    monthly_spend_requirement = spend_requirement / 3  # Typically 3 months
    
    eligible = total_monthly_spend >= monthly_spend_requirement if monthly_spend_requirement > 0 else False
    
    return {
        'value': signup_bonus,
        'spend_requirement': spend_requirement,
        'monthly_spend_requirement': monthly_spend_requirement,
        'eligible': eligible,
    }

