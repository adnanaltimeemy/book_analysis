def estimate_savings(current_data, target_literacy_rate_percent):
    """
    Estimate the economic savings if literacy rate improves from current to target.
    """
    if target_literacy_rate_percent <= current_data.literacy_rate_percent:
        print(f"Target literacy rate must be higher than current ({current_data.literacy_rate_percent}%). No savings.")
        return 0
    
    illiterate_current = 100 - current_data.literacy_rate_percent
    illiterate_target = 100 - target_literacy_rate_percent
    
    reduction_ratio = illiterate_target / illiterate_current
    estimated_new_cost = current_data.annual_cost_usd * reduction_ratio
    
    savings = current_data.annual_cost_usd - estimated_new_cost
    
    print(f"{current_data.name}:")
    print(f"  Current literacy: {current_data.literacy_rate_percent}%")
    print(f"  Target literacy: {target_literacy_rate_percent}%")
    print(f"  Estimated annual economic cost after improvement: ${estimated_new_cost:,.0f}")
    print(f"  Estimated annual savings: ${savings:,.0f}")
    
    return savings

# Example: Estimate savings if US literacy improves from 46% to 60%
estimate_savings(countries[0], 60)
