"""
Card ranking algorithm based on reward optimization.
"""
from typing import List, Dict, Any
from services.reward_calculator import calculate_total_rewards, calculate_signup_bonus_value


def rank_cards(
    cards: List[Dict[str, Any]],
    spend: Dict[str, float]
) -> List[Dict[str, Any]]:
    """
    Rank cards based on total reward value.
    
    Args:
        cards: List of card dictionaries
        spend: Dictionary of category -> monthly spend
    
    Returns:
        List of ranked cards with reward calculations
    """
    total_monthly_spend = sum(spend.values())
    
    ranked_cards = []
    
    for card in cards:
        # Calculate rewards
        reward_data = calculate_total_rewards(card, spend)
        
        # Calculate signup bonus
        signup_bonus_data = calculate_signup_bonus_value(card, total_monthly_spend)
        
        # Determine category strengths (top 2 categories by reward rate)
        category_rewards = card.get('category_rewards', {})
        category_strengths = sorted(
            category_rewards.items(),
            key=lambda x: x[1],
            reverse=True
        )[:2]
        strengths = [cat.lower() for cat, _ in category_strengths]
        
        # Calculate total first-year value (including signup bonus)
        first_year_value = reward_data['net_annual_rewards']
        if signup_bonus_data['eligible']:
            first_year_value += signup_bonus_data['value']
        
        ranked_cards.append({
            'card_name': card['name'],
            'issuer': card.get('issuer', 'Unknown'),
            'reward_value_monthly': reward_data['monthly_rewards'],
            'reward_value_yearly': reward_data['annual_rewards'],
            'net_annual_rewards': reward_data['net_annual_rewards'],
            'category_strengths': strengths,
            'signup_bonus_value': signup_bonus_data['value'] if signup_bonus_data['eligible'] else 0,
            'effective_annual_fee': reward_data['effective_annual_fee'],
            'overall_rate': reward_data['overall_rate'],
            'first_year_value': round(first_year_value, 2),
            'category_breakdown': reward_data['category_breakdown'],
            'signup_bonus_eligible': signup_bonus_data['eligible'],
            'card_data': card,
        })
    
    # Sort by first-year value (best overall value)
    ranked_cards.sort(key=lambda x: x['first_year_value'], reverse=True)
    
    return ranked_cards


def generate_explanation(
    best_card: Dict[str, Any],
    spend: Dict[str, float]
) -> str:
    """
    Generate explanation for why a card is optimal.
    
    Args:
        best_card: Best card dictionary
        spend: Spending breakdown
    
    Returns:
        Explanation string
    """
    card_name = best_card['card_name']
    strengths = best_card['category_strengths']
    monthly_rewards = best_card['reward_value_monthly']
    annual_rewards = best_card['reward_value_yearly']
    annual_fee = best_card['effective_annual_fee']
    signup_bonus = best_card.get('signup_bonus_value', 0)
    
    explanation_parts = [
        f"{card_name} is optimal for your spending profile because:"
    ]
    
    if strengths:
        explanation_parts.append(
            f"- Strong rewards in {', '.join(strengths)} categories"
        )
    
    explanation_parts.append(
        f"- Estimated ${monthly_rewards:.2f}/month (${annual_rewards:.2f}/year) in rewards"
    )
    
    if annual_fee > 0:
        explanation_parts.append(f"- After ${annual_fee:.2f} annual fee: ${annual_rewards - annual_fee:.2f}/year net")
    else:
        explanation_parts.append("- No annual fee")
    
    if signup_bonus > 0 and best_card.get('signup_bonus_eligible'):
        explanation_parts.append(
            f"- Eligible for ${signup_bonus:.2f} signup bonus (first year value: ${best_card['first_year_value']:.2f})"
        )
    
    return " ".join(explanation_parts)


