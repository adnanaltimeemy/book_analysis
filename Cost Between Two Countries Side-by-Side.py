def compare_countries(country1, country2):
    print(f"Comparing {country1.name} vs {country2.name}:")
    
    illiterate1 = 100 - country1.literacy_rate_percent
    illiterate2 = 100 - country2.literacy_rate_percent
    
    print(f"Illiterate population %: {country1.name}: {illiterate1}%, {country2.name}: {illiterate2}%")
    
    print(f"Annual economic cost (USD): {country1.name}: ${country1.annual_cost_usd:,.0f}, {country2.name}: ${country2.annual_cost_usd:,.0f}")
    
    if country1.annual_cost_usd > country2.annual_cost_usd:
        print(f"{country1.name} suffers higher economic losses due to literacy.")
    else:
        print(f"{country2.name} suffers higher economic losses due to literacy.")

# Example:
compare_countries(countries[0], countries[1])
